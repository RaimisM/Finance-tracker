from income_tracker import IncomeTracker
from expense_tracker import ExpenseTracker
from transaction_editor import TransactionManager
from visual_manager import VisualManager
from file_manager import FileManager

def main():
    income_tracker = IncomeTracker()
    expense_tracker = ExpenseTracker()
    transaction_manager = TransactionManager()
    visual_manager = VisualManager()
    file_manager = FileManager("money.csv")

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance and Summary")
        print("4. Edit Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_income(income_tracker, file_manager)
        elif choice == "2":
            add_expense(expense_tracker, file_manager)
        elif choice == "3":
            show_balance_and_summary(visual_manager)
        elif choice == "4":
            edit_transactions(transaction_manager)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_income(income_tracker, file_manager):
    print("\nAdd Income")
    while True:
        try:
            category = income_tracker.income_categories()
            amount = file_manager.get_amount()
            description = file_manager.get_description()
            
            if confirm_transaction("Income", category, amount, description, file_manager):
                print("Income added successfully! ✅")
        except ValueError as e:
            print(f"Error: {e}")

        while True:
            another = input("Do you want to add another income? (yes/no): ").strip().lower()
            if another in ["yes", "y"]:
                break
            elif another in ["no", "n"]:
                return
            else:
                print("Invalid input. Please type 'yes' or 'no'")

def add_expense(expense_tracker, file_manager):
    print("\nAdd Expense")
    while True:
        try:
            category = expense_tracker.expense_categories()
            amount = file_manager.get_amount()
            description = file_manager.get_description()

            if confirm_transaction("Expense", category, amount, description, file_manager):
                print("Expense added successfully! ✅")
        except ValueError as e:
            print(f"Error: {e}")

        while True:
            another = input("Do you want to add another expense? (yes/no): ").strip().lower()
            if another in ["yes", "y"]:
                break
            elif another in ["no", "n"]:
                return
            else:
                print("Invalid input. Please type 'yes' or 'no'")

def confirm_transaction(transaction_type, category, amount, description, file_manager):
    print("\nPlease confirm the details:")
    print(f"\tType: {transaction_type}")
    print(f"\tCategory: {category}")
    print(f"\tAmount: €{amount:.2f}")
    print(f"\tDescription: {description}")

    while True:
        confirm = input("Do you want to add this transaction? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            file_manager.add_transaction(transaction_type, category, amount, description)
            return True
        elif confirm in ["no", "n"]:
            print(f"{transaction_type} not added. ⛔")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'")

def show_balance_and_summary(visual_manager):
    print("\nView Balance and Summary")
    while True:
        print("Select a timeframe:")
        print("1. This month")
        print("2. This year")
        print("3. Custom date")
        print("4. All Time")
        print("5. Back")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            visual_manager.show_summary("month")
        elif choice == "2":
            visual_manager.show_summary("year")
        elif choice == "3":
            visual_manager.show_summary("custom_date")
        elif choice == "4":
            visual_manager.show_summary("all")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def edit_transactions(transaction_manager):
    print("\nEdit Transactions")
    while True:
        print("1. View Transactions")
        print("2. Edit a Transaction")
        print("3. Delete a Transaction")
        print("4. Back")

        choice = input("Select an option: ").strip()
        if choice == "1":
            transaction_manager.display_data()
        elif choice == "2":
            transaction_manager.edit_data()
        elif choice == "3":
            transaction_manager.delete_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
