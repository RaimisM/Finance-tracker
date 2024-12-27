from file_manager import FileManager

class IncomeTracker:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)
        self.file_manager.create_file(["ID", "Date", "Type", "Category", "Amount", "Description"])


    @staticmethod
    def income_categories():
        valid_categories = {
        "Salary": "💼",
        "Gift": "🎁",
        "Interest": "💰",
        "Other": "🔧"
    }
        print("Available income categories:")

        for i, (category, emoji) in enumerate(valid_categories.items(), 1,):
            print(f"{i}. {emoji} {category}")

        while True:
            try:
                choice = int(input("Enter category number: "))
                if 1 <= choice <= len(valid_categories):
                    return list(valid_categories.keys())[choice - 1]
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid category. Please try again.")
    
