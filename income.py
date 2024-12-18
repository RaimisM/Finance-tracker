from datetime import datetime
import csv

class IncomeTracker:
    def __init__(self, filename='income.csv'):
        self.filename = filename
        self._file_manager()

    def _file_manager(self):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Category", "Amount", "Description", "Date"])

    def add_income(self, category, amount, description, date):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, amount, description, current_date])
        print("Income added successfully!")

    @staticmethod
    def get_categories():
        category = input("Select income category (Salary, Gift, Interest, Others): ").strip().lower()
        while category not in ["salary", "gift", "interest", "others"]:
            category = input("Invalid category. Please try again: ").strip().lower()
        return category
    
    @staticmethod
    def get_amount():
        try:
            amount = float(input("Enter amount: "))
            return amount
        except ValueError:
            print("Invalid amount. Please try again.")
            return None
        
    @staticmethod
    def get_description():
        return input("Enter description: ").strip()
    
def main():
    tracker = IncomeTracker()
    category = tracker.get_categories()
    amount = tracker.get_amount()
    if amount is None:
        return
    description = tracker.get_description()
    tracker.add_income(category, amount, description, datetime.now())   

if __name__ == "__main__":
    main()

            
