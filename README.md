# Personal Finance Tracker

This project is a simple command-line application for managing personal finances. It allows you to track income and expenses, edit or delete transactions, and generate summaries based on various time frames (e.g., monthly, yearly). The data is stored in a CSV file and can be filtered, displayed, and modified interactively.

## Installation

This project requires Python 3 and the following libraries:
*   pandas
*   pytest
You can install the required packages using pip:
```bash
pip install pandas
pip install pytest
```
## **Usage**

To use Personal Finance Tracker, follow these steps:

1. Open the project in your favorite code editor.
2. Start the project: **`python main.py`**
3. Use the project to manage your finances.

## Features

- **Add Transactions**: Add income and expense transactions, select catagories and amounts.
- **Edit Transactions**: Modify existing transactions including the date, type, category, amount, and description.
- **Delete Transactions**: Remove unwanted transactions from the record.
- **Display Transactions**: View all transactions in a sorted format.
- **Data Filtering**: Filter transactions by month, year, or custom date range.
- **Data Summary**: View summaries of income and expenses by category, including total balance calculations.
- **File Management**: Automatically load and save data to a CSV file.

## Project Structure

- `main.py`: The entry point for the application, handling user interactions and running the program.
- `file_manager.py`: Contains the `FileManager` class, which is responsible for loading and saving data to the CSV file.
- `income_tracker.py`: Contains the `IncomeTracker` class, responsible for tracking and managing income transactions.
- `expense_tracker.py`: Contains the `ExpenseTracker` class, responsible for tracking and managing expense transactions.
- `visual_manager.py`: Handles the visual display and filtering of data.
- `transaction_editor.py`: Manages editing and deleting transactions.
- `money.csv`: The CSV file where transaction data is stored.
- `requirements.txt`: The text file lists all the dependencies of the project.
- `test_main.py`: Contains tests for the `main.py`.
- `test_visual_manager.py`: Contains tests for the `visual_manager.py`.
- `test_transaction_editor.py`: Contains tests for the `transaction_editor.py`.



