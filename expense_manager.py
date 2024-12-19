from datetime import datetime
import csv

class ExpenseTracker:
    def __init__(self, filename='expense.csv'):
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

    def add_expense(self, category, amount, description):
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\nExpense details:")
        print(f"\tCategory: {category}")
        print(f"\tAmount: {amount:.2f} EUR")
        print(f"\tDescription: {description.capitalize()}")

        while True:
            confirm = input("Do you want to add this expense? (yes/no): ").strip().lower()
            if confirm in ["yes", "y"]:
                try:
                    with open(self.filename, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([unique_id, current_date, category, amount, description])
                    print("Expense added successfully!")
                except Exception as e:
                    print(f"An error occurred: {e}")
                return
            elif confirm in ["no", "n"]:
                print("Expense not added.")
                return
            else:
                print("Invalid input. Please type 'yes', 'y', 'no', or 'n'.")


    @staticmethod
    def get_categories():
        categories = {
            "Food": "🍔",
            "Transport": "🚗",
            "Entertainment": "🎥",
            "Health": "💊",
            "Education": "📚",
            "Comunication": "📱",
            "Home": "🏠",
            "Clothing": "👕",
            "Gifts": "🎁",
            "Travel": "🌍",
            "Beauty": "💅",
            "Pets": "🐶",
            "Sport": "🏀",
            "Social": "🎉",
            "Holidays": "🏖️",
            "Donations": "🎗️",
            "Others": "💸"
        }
        print("Select expense category:")
        for i, (category, emoji) in enumerate(categories.items(), 1,):
            print(f"{i}. {category} {emoji}")

        while True:
            try:
                choice = int(input("Enter category number: "))
                if 1 <= choice <= len(categories):
                    selected_category = list(categories.keys())[choice - 1]
                    return selected_category
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid category. Please try again.")


    @staticmethod
    def get_amount():
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    return amount
                else:
                    print("Amount must be greater than zero. Please try again.")
            except ValueError:
                print("Invalid amount. Please try again.")

    @staticmethod
    def get_description():
        return input("Enter description: ").strip()
    
def main():
    tracker = ExpenseTracker()
    while True:
        category = tracker.get_categories()
        amount = tracker.get_amount()
        description = tracker.get_description()
        tracker.add_expense(category, amount, description)

        while True:
            another_expense = input("Do you want to add another expense? (yes/no): ").strip().lower()
            if another_expense in ["yes", "y"]:
                break
            elif another_expense in ["no", "n"]:
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please type 'yes', 'y', 'no', or 'n'.")


if __name__ == "__main__":
    main()