from income_tracker import IncomeTracker
from expense_tracker import ExpenseTracker
from transaction_editor import TransactionManager
from visual_manager import VisualManager

def main():
    income_tracker = IncomeTracker()
    expense_tracker = ExpenseTracker()
    transaction_manager = TransactionManager()
    visual_manager = VisualManager()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance and Summary")
        print("4. Edit Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_income(income_tracker)
        elif choice == "2":
            add_expense(expense_tracker)
        elif choice == "3":
            show_balance_and_summary(visual_manager)
        elif choice == "4":
            edit_transactions(transaction_manager)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_income(income_tracker):
    print("\nAdd Income")
    while True:
        category = income_tracker.income_categories()
        amount = income_tracker.file_manager.get_amount()
        description = income_tracker.file_manager.get_description()
        income_tracker.file_manager.add_transaction("Income", category, amount, description)

        another = input("Do you want to add another income? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            break

def add_expense(expense_tracker):
    print("\nAdd Expense")
    while True:
        category = expense_tracker.expense_categories()
        amount = expense_tracker.file_manager.get_amount()
        description = expense_tracker.file_manager.get_description()
        expense_tracker.file_manager.add_transaction("Expense", category, amount, description)

        another = input("Do you want to add another expense? (yes/no): ").strip().lower()
        if another not in ["yes", "y"]:
            break

def show_balance_and_summary(visual_manager):
    print("\nView Balance and Summary")
    while True:
        print("1. This Month")
        print("2. This Year")
        print("3. All Time")
        print("4. Back")

        choice = input("Select a timeframe: ").strip()
        if choice == "1":
            visual_manager.show_summary("month")
        elif choice == "2":
            visual_manager.show_summary("year")
        elif choice == "3":
            visual_manager.show_summary("all")
        elif choice == "4":
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
