import os
from file_manager import FileManager

def main():
    setup_function()
    test_add_income()
    test_add_expense()

def setup_function():
    with open("test_money.csv", "w") as file:
        headers = ["ID", "Date", "Type", "Category", "Amount", "Description"]
        file.write(",".join(headers) + "\n")

def test_add_income():
    file_manager = FileManager("test_money.csv")
    file_manager.add_transaction("Income", "Salary", 1000.0, "Monthly Salary")
    data = file_manager.load_data()
    
    assert len(data) == 1
    assert data[0]["Type"] == "Income"
    assert data[0]["Category"] == "Salary"
    assert float(data[0]["Amount"]) == 1000.0

def test_add_expense():
    file_manager = FileManager("test_money.csv")
    file_manager.add_transaction("Expense", "Groceries", 50.0, "Weekly Groceries")
    data = file_manager.load_data()

    assert len(data) == 1
    assert data[0]["Type"] == "Expense"
    assert data[0]["Category"] == "Groceries"
    assert float(data[0]["Amount"]) == 50.0


if __name__ == "__main__":
    main()
