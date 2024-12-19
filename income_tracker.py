from datetime import datetime
import csv

class IncomeTracker:
    def __init__(self, filename='income.csv'):
        self.filename = filename
        self._file_manager()

    def _file_manager(self):
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(["ID", "Date", "Category", "Amount", "Description"])
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_income(self, category, amount, description):
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([unique_id, current_date, category, amount, description])
            print("Income added successfully!")
        except Exception as e:
            print(f"Error adding income: {e}")


    @staticmethod
    def get_categories():
        category = input("Select income category (Salary, Gift, Interest, Others): ").strip().lower()
        while category not in ["salary", "gift", "interest", "others"]:
            category = input("Invalid category. Please try again: ").strip().lower()
        return category
    
    @staticmethod
    def get_amount():
        while True:
            try:
                amount = float(input("Enter amount: "))
                while amount <= 0:
                    amount = float(input("Invalid amount. Please try again: "))
                return amount
            except ValueError:
                print("Invalid amount. Please try again.")
                continue

    @staticmethod
    def get_description():
        return input("Enter description: ").strip()
    
def main():
    tracker = IncomeTracker()
    while True:
        category = tracker.get_categories()
        amount = tracker.get_amount()
        description = tracker.get_description()
        tracker.add_income(category, amount, description)

        while True:
            answer = input("Do you want to add another income? (yes/no): ").strip().lower()
            if answer in ["yes", "y"]:
                break
            elif answer in ["no", "n"]:
                print("Thank you for using the Income Tracker. Goodbye!")
                return
            else:
                print("Invalid input. Please type 'yes', 'y', 'no', or 'n'.")

        
if __name__ == "__main__":
    main()

            
