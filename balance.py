from datetime import datetime, timedelta
import csv

class BalanceTracker:
    def __init__(self, expense_file='expense.csv', income_file='income.csv'):
        self.expense_file = expense_file
        self.income_file = income_file

    def load_date(self):
        data = []
        try:
            with open(self.expense_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append({
                        "ID": row["ID"],
                        "Date": row["Date"],
                        "Type": "Expense",
                        "Category": row["Category"],
                        "Amount": "-{:.2f}".format(float(row["Amount"])),
                        "Description": row["Description"]
                    })

            with open(self.income_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append({
                        "ID": row["ID"],
                        "Date": row["Date"],
                        "Type": "Income",
                        "Category": row["Category"],
                        "Amount": "+{:.2f}".format(float(row["Amount"])),
                        "Description": row["Description"]
                    })
        except Exception as e:
            print(f"An error occurred: {e}")
        return data
    
    def filter_data(self, data, filter_type):
        now = datetime.now()
        if filter_type == "this_year":
            start_date = datetime(now.year, 1, 1)
        elif filter_type == "this_month":
            start_date = datetime(now.year, now.month, 1)
        elif filter_type == "this_week":
            start_date = now - timedelta(days=now.weekday())
        elif filter_type == "today":
            start_date = datetime(now.year, now.month, now.day)
        else:
            return data
        
        filtered_data = [
            item for item in data if start_date <= datetime.strptime(item["Date"], "%Y-%m-%d %H:%M:%S")
        ]
        return filtered_data
    
    def display_data(self, data):
        if not data:
            print("No data available.")
            return
        
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x["Date"], "%Y-%m-%d %H:%M:%S"))
        print(f"{'\nID':<20}{'Date':<30}{'Type':<15}{'Category':<15}{'Amount':<15}{'Description'}")
        print("-" * 100)

        for item in sorted_data:
            print(f"{item['ID']:<20}{item['Date']:<30}{item['Type']:<15}{item['Category']:<15}{item['Amount']:<15}{item['Description']}")




def main():
    tracker = BalanceTracker()
    print("Do you want to see:")
    print("1. All records")
    print("2. Records for this year")
    print("3. Records for this month")
    print("4. Records for this week")
    print("5. Today's records")
    choice = input("Enter your choice (1-5): ").strip()

    filter_map = {
        "1": "all",
        "2": "this_year",
        "3": "this_month",
        "4": "this_week",
        "5": "today"
    }
    filter_type = filter_map.get(choice, "all")
    data = tracker.load_date()
    filtered_data = tracker.filter_data(data, filter_type)
    tracker.display_data(filtered_data)

if __name__ == "__main__":
    main()

