from file_manager import FileManager

class IncomeTracker:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)
        self.file_manager.create_file(["ID", "Date", "Type", "Category", "Amount", "Description"])


    @staticmethod
    def income_categories():
        valid_categories = ["salary", "gift", "interest", "others"]
        print("Available income categories:", ", ".join(valid_categories))
        category = input("Select income category: ").strip().capitalize
        while category not in valid_categories:
            category = input("Invalid category. Please try again: ").strip().lower()
        return category
    

    
def add_income(self):
        category = self.income_categories()
        amount = self.file_manager.get_amount()
        description = self.file_manager.get_description()
        self.file_manager.add_transaction("Income", category, amount, description)
        print("Income added successfully!")

            
