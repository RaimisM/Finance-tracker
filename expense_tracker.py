from file_manager import FileManager

class ExpenseTracker:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)
        self.file_manager.create_file(["ID", "Date", "Type", "Category", "Amount", "Description"])

    @staticmethod
    def expense_categories():
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
                    return list(categories.keys())[choice - 1]
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid category. Please try again.")

   
def main():
    tracker = ExpenseTracker()
    while True:
        category = tracker.expense_categories()
        amount = tracker.file_manager.get_amount()
        description = tracker.file_manager.get_description()
        tracker.file_manager.add_transaction("Expense", category, amount, description)

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