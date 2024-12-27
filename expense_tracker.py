from file_manager import FileManager

class ExpenseTracker:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)
        self.file_manager.create_file(["ID", "Date", "Type", "Category", "Amount", "Description"])

    @staticmethod
    def expense_categories():
        categories = {
            "Home": "🏠",
            "Food": "🍔",
            "Transport": "🚗",
            "Entertainment": "🎥",
            "Health": "💊",
            "Education": "📚",
            "Comunication": "📱",
            "Clothing": "👕",
            "Gifts": "🎁",
            "Travel": "🌍",
            "Beauty": "💅",
            "Pets": "🐶",
            "Sport": "🏀",
            "Social": "🎉",
            "Donations": "🎗️",
            "Other": "💸"
        }
        print("Select expense category:")
        for i, (category, emoji) in enumerate(categories.items(), 1,):
            print(f"{i}. {emoji} {category}")

        while True:
            try:
                choice = int(input("Enter category number: "))
                if 1 <= choice <= len(categories):
                    return list(categories.keys())[choice - 1]
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid category. Please try again.")

   
