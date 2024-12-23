from file_manager import FileManager

class IncomeTracker:
    def __init__(self, filename='money.csv'):
        self.file_manager = FileManager(filename)
        self.file_manager.create_file(["ID", "Date", "Type", "Category", "Amount", "Description"])


    @staticmethod
    def income_categories():
        valid_categories = ["salary", "gift", "interest", "other"]
        print("Available income categories:", ", ".join([category.capitalize() for category in valid_categories]))
        while True:
            category = input("Select income category: ").strip().lower()
            if category in valid_categories:
                return category.capitalize()
            else:
                print("Invalid category. Please try again.")
    

    
# def main():
#     tracker = IncomeTracker()
#     while True:
#         category = tracker.income_categories()
#         amount = tracker.file_manager.get_amount()
#         description = tracker.file_manager.get_description()
#         tracker.file_manager.add_transaction("Income", category, amount, description)

#         while True:
#             answer = input("Do you want to add another income? (yes/no): ").strip().lower()
#             if answer in ["yes", "y"]:
#                 break
#             elif answer in ["no", "n"]:
#                 print("Thank you for using the Income Tracker. Goodbye!")
#                 return
#             else:
#                 print("Invalid input. Please select yes or no.")

        
# if __name__ == "__main__":
#     main()

            
