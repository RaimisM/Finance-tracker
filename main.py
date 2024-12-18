




def main():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Balance")
    print("5. Vizualize Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Select category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        date = input("Enter date: ")
        add_income(category, amount, description, date)
    elif choice == "2":
        category = input("Select category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        date = input("Enter date: ")
        add_expense(category, amount, description, date)
    elif choice == "3":
        show_transactions()
    elif choice == "4":
        show_balance()
    elif choice == "5":
        visualize_data()
    elif choice == "6":
        print("Exiting...")
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


