import pandas as pd
from datetime import datetime
import os
import calendar

class VisualManager:
    def __init__(self, filename="money.csv"):
        self.filename = filename
        self.last_modified_time = None
        self.data = self.load_data()
    
    def get_file_modification_time(self):
        try:
            return os.path.getmtime(self.filename)
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            return None

    def load_data(self):
        try:
            data = pd.read_csv(self.filename)
            data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
            data["Amount"] = pd.to_numeric(data["Amount"], errors='coerce')
            self.last_modified_time = self.get_file_modification_time()
            return data
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            return pd.DataFrame()

    def check_and_reload_data(self):
        current_modified_time = self.get_file_modification_time()
        if current_modified_time != self.last_modified_time:
            self.data = self.load_data()

    def filter_data(self, timeframe):
        self.check_and_reload_data()
        now = datetime.now()
        if timeframe == "month":
            return self.data[self.data["Date"].dt.month == now.month]
        elif timeframe == "year":
            return self.data[self.data["Date"].dt.year == now.year]
        elif timeframe == "custom_date":
            available_years = self.data["Date"].dt.year.dropna().unique()
            available_years.sort()
            print("Available years:")
            for year in available_years:
                print(f"\t{year}")
            
            while True:
                try:
                    selected_year = int(input("Enter the year: ").strip())
                    if selected_year not in available_years:
                        print(f"Year {selected_year} is not available. Please select a valid year from above. 🢁")
                    else:
                        break
                except ValueError:
                    print("Invalid year. Please see the available year above. 🢁")

            available_months = self.data[self.data["Date"].dt.year == selected_year]["Date"].dt.month.dropna().unique()
            available_months.sort()
            month_names = [calendar.month_name[month] for month in available_months]
            month_names.append("Full Year")
            print("Available months:")
            for month in month_names:
                print(f"\t{month}")

            while True:
                try:
                    selected_month = input("Enter the month (e.g., January or Full Year): ").strip().title()
                    if selected_month == "Full Year":
                        return self.data[self.data["Date"].dt.year == selected_year], None, selected_year
                    elif selected_month not in month_names:
                        print(f"Month {selected_month} is not available for year {selected_year}. Please select a valid month.")
                    else:
                        selected_month = list(calendar.month_name).index(selected_month)
                        return self.data[(self.data["Date"].dt.year == selected_year) & (self.data["Date"].dt.month == selected_month)], calendar.month_name[selected_month], selected_year
                except ValueError:
                    print("Invalid selection. Please try again.")
        
        elif timeframe == "all":
            return self.data
        else:
            print("Invalid timeframe selection.")
            return pd.DataFrame()

    def summarize_data(self, data, month=None, year=None):
        if data.empty:
            print("No transactions available.")
            return
        
        if month and year:
            print(f"\nSummary for {month} {year}:")
        elif month:
            print(f"\nSummary for {month}:")
        elif year:
            print(f"\nSummary for {year}:")
        
        income = data[data["Type"] == "Income"].groupby("Category")["Amount"].sum()
        expenses = data[data["Type"] == "Expense"].groupby("Category")["Amount"].sum()
        total_income = income.sum()
        total_expenses = expenses.sum()
        balance = total_income - total_expenses

        print("\nIncome by Category:")
        if not income.empty:
            for category, amount in income.items():
                print(f"{category}: €{amount:.2f}")
        else:
            print("No income recorded.")

        print("\nExpenses by Category:")
        if not expenses.empty:
            for category, amount in expenses.items():
                print(f"{category}: €{amount:.2f}")
        else:
            print("No expenses recorded.")

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
        if timeframe == "custom_date":
            filtered_data, selected_month, selected_year = self.filter_data(timeframe)
            self.summarize_data(filtered_data, selected_month, selected_year)
        else:
            filtered_data = self.filter_data(timeframe)
            self.summarize_data(filtered_data)
