import pandas as pd
from datetime import datetime

class VisualManager:
    def __init__(self, filename="money.csv"):
        self.filename = filename
        try:
            self.data = self.load_data()
            if not self.data.empty:
                self.data["Date"] = pd.to_datetime(self.data["Date"], errors='coerce')
                self.data["Amount"] = pd.to_numeric(self.data["Amount"], errors='coerce')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.data = pd.DataFrame()

    def load_data(self):
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            return pd.DataFrame()

    def filter_data(self, timeframe):
        now = datetime.now()
        if timeframe == "month":
            return self.data[self.data["Date"].dt.month == now.month]
        elif timeframe == "year":
            return self.data[self.data["Date"].dt.year == now.year]
        elif timeframe == "all":
            available_years = self.data["Date"].dt.year.dropna().unique()
            available_years.sort()
            print("Available years:", ", ".join(map(str, available_years)))
            try:
                selected_year = int(input("Enter the year: ").strip())
                if selected_year in available_years:
                    return self.data[self.data["Date"].dt.year == selected_year]
                else:
                    print(f"Year {selected_year} is not available.")
                    return pd.DataFrame()
            except ValueError:
                print("Invalid year selection. Please try again.")
                return pd.DataFrame()
        else:
            print("Invalid timeframe selection.")
            return pd.DataFrame()

    def summarize_data(self, data):
        if data.empty:
            print("No transactions available.")
            return
        
        income = data[data["Type"] == "Income"].groupby("Category")["Amount"].sum()
        expenses = data[data["Type"] == "Expense"].groupby("Category")["Amount"].sum()
        total_income = income.sum()
        total_expenses = expenses.sum()
        balance = total_income - total_expenses

        print("\nSummary:")
        print("\nIncome by Category:")
        if not income.empty:
            for category, amount in income.items():
                print(f"  {category}: €{amount:.2f}")
        else:
            print("No income recorded.")

        print("\nExpenses by Category:")
        if not expenses.empty:
            for category, amount in expenses.items():
                print(f"  {category}: €{amount:.2f}")
        else:
            print("  No expenses recorded.")

        print(f"\nTotal Income: €{total_income:.2f}")
        print(f"Total Expenses: €{total_expenses:.2f}")
        if balance > 0:
            print(f"Balance: €\033[92m{balance:.2f}\033[0m")
        elif balance < 0:
            print(f"Balance: €\033[91m{balance:.2f}\033[0m")
        else:
            print(f"Balance: €{balance:.2f}")
        print("\n")

    def show_summary(self, timeframe):
        filtered_data = self.filter_data(timeframe)
        self.summarize_data(filtered_data)

if __name__ == "__main__":
    visual_manager = VisualManager()

    while True:
        print("\nSelect a timeframe:")
        print("1. This month")
        print("2. This year")
        print("3. All time")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            visual_manager.show_summary("month")
        elif choice == "2":
            visual_manager.show_summary("year")
        elif choice == "3":
            visual_manager.show_summary("all")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
