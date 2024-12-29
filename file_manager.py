import csv
from datetime import datetime

class FileManager:
    def __init__(self, filename):
        self.filename = filename


    def create_file(self, headers):
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(headers)
        except Exception as e:
            print(f"An error occurred: {e}")


    def load_data(self):
        data = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print("File not found.")
        return data
    

    def save_data(self, data):
        try:
            headers = ["ID", "Date", "Type", "Category", "Amount", "Description"]
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"An error occurred: {e}")


    def add_transaction(self, transaction_type, category, amount, description):
        try:
            unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = {
                "ID": unique_id,
                "Date": current_date,
                "Type": transaction_type,
                "Category": category,
                "Amount": "{:.2f}".format(amount),
                "Description": description
            }
            data = self.load_data()
            data.append(entry)
            self.save_data(data)

        except Exception as e:
            print(f"An error occurred: {e}")

   
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
        return input("Enter description: ").strip().title()