from datetime import datetime
from file_manager import FileManager

class TransactionManager:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)

    def edit_data(self):
        data = self.file_manager.load_data()
        if not data:
            print("No transactions available to edit.")
            return

        transaction_id = input("Enter the ID of the record you want to edit: ").strip()
        transaction = next((item for item in data if item["ID"] == transaction_id), None)

        if not transaction:
            print("Record not found.")
            return
        original_transaction = transaction.copy()

        print("\nTransaction details:")
        for key, value in transaction.items():
            print(f"\t{key}: {value}")


        while True:
            new_date = input(
                f"Enter new date in YYYY-MM-DD format (leave blank to keep current: {transaction['Date']}): "
            ).strip()
            if not new_date:
                break
            try:
                new_year, new_month, new_day = map(int, new_date.split("-"))
                if new_year < 2000:
                    print("Year cannot be earlier than 2000. Please try again.")
                elif 1 <= new_month <= 12 and 1 <= new_day <= 31:
                    transaction["Date"] = f"{new_year:04d}-{new_month:02d}-{new_day:02d} {transaction['Date'].split(' ')[1]}"
                    break
                else:
                    print("Invalid month or day. Please try again.")
            except ValueError:
                print("Invalid date format. Please try again.")

        while True:
            new_type = input(f"Enter new type (Income/Expense, leave blank to keep current: {transaction['Type']}): ").strip()
            if not new_type:
                break
            if new_type in ["Income", "Expense"]:
                transaction["Type"] = new_type
                break
            else:
                print("Invalid type. Please enter 'Income' or 'Expense'.")

        if transaction["Type"] == "Income":
            print("Available income categories: Salary, Gift, Interest, Other")
        else:
            print("Available expense categories: Food, Transport, Entertainment, Health, Education, Communication, Home, Clothing, Gifts, Travel, Beauty, Pets, Sport, Social, Holidays, Donations, Other")

        while True:
            new_category = input(f"Enter new category (leave blank to keep current: {transaction['Category']}): ").strip()
            if not new_category:
                break

            if transaction["Type"] == "Income" and new_category.capitalize() in ["Salary", "Gift", "Interest", "Other"]:
                transaction["Category"] = new_category.capitalize()
                break
            elif transaction["Type"] == "Expense" and new_category.capitalize() in [
                "Food", "Transport", "Entertainment", "Health", "Education", "Communication", "Home", "Clothing", "Gifts",
                "Travel", "Beauty", "Pets", "Sport", "Social", "Holidays", "Donations", "Other"
            ]:
                transaction["Category"] = new_category.capitalize()
                break
            else:
                print("Invalid category. Please try again.")

        while True:
            new_amount = input(f"Enter new amount (leave blank to keep current: {transaction['Amount']}): ").strip()
            if not new_amount:
                break
            try:
                new_amount = float(new_amount)
                if new_amount < 0:
                    print("Amount cannot be less than 0. Please try again.")
                else:
                    transaction["Amount"] = f"{new_amount:.2f}"
                    break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")


        new_description = input(f"Enter new description (leave blank to keep current: {transaction['Description']}): ").strip()
        if new_description:
            transaction["Description"] = new_description

        print("\nUpdated transaction details:")
        for key, value in transaction.items():
            if value != original_transaction[key]:
                print(f"\t\033[33m{key}: {value} (Changed)\033[0m")
            else:
                print(f"\t{key}: {value}")


        if input("Do you want to save changes? (yes/no): ").strip().lower() in ["yes", "y"]:
            self.file_manager.save_data(data)
            print("Record updated successfully.")
        else:
            print("Changes not saved.")




    def delete_data(self):
        data = self.file_manager.load_data()
        if not data:
            print("No transactions available to delete.")
            return

        transaction_id = input("Enter the ID of the record you want to delete: ").strip()
        transaction = next((item for item in data if item["ID"] == transaction_id), None)

        if not transaction:
            print("Record not found.")
            return

        print("\nTransaction details:")
        for key, value in transaction.items():
            print(f"\t{key}: {value}")

        if input("Do you want to delete this record? (yes/no): ").strip().lower() in ["yes", "y"]:
            data.remove(transaction)
            self.file_manager.save_data(data)
            print("Record deleted successfully.")
        else:
            print("Record not deleted.")

    def display_data(self):
        data = self.file_manager.load_data()
        if not data:
            print("No transactions available.")
            return

        sorted_data = sorted(data, key=lambda x: datetime.strptime(x["Date"], "%Y-%m-%d %H:%M:%S"))
        print(f"{'ID':<20}{'Date':<30}{'Type':<15}{'Category':<15}{'Amount':<15}{'Description'}")
        print("-" * 110)

        for item in sorted_data:
            print(f"{item['ID']:<20}{item['Date']:<30}{item['Type']:<15}{item['Category']:<15}{item['Amount']:<15}{item['Description']}")

def main():
    manager = TransactionManager()
    while True:
        print("\nOptions:")
        print("1. View transactions")
        print("2. Edit a transaction")
        print("3. Remove a transaction")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.display_data()
        elif choice == "2":
            manager.edit_data()
        elif choice == "3":
            manager.delete_data()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
