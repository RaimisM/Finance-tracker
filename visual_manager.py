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
        return self.data

    def summarize_data(self, data):
        income = data[data["Type"] == "Income"]["Amount"].sum()
        expenses = data[data["Type"] == "Expense"]["Amount"].sum()
        print(f"Total Income: €{income:.2f}, Total Expenses: €{expenses:.2f}, Balance: €{income - expenses:.2f}")