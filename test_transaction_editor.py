import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from transaction_editor import TransactionManager


def main():
    test_edit_data()
    test_delete_data()

def test_edit_data():
    manager = TransactionManager("test_money.csv")
    with patch("builtins.input", side_effect=["1", "2023-12-01", "income", "salary", "2000.0", "Updated Description", "y"]):
        with patch.object(manager.file_manager, "load_data", return_value=[{"ID": "1", "Date": "2023-11-01 12:00:00", "Type": "Expense", "Category": "Food", "Amount": "50.0", "Description": "Lunch"}]):
            with patch.object(manager.file_manager, "save_data", MagicMock()):
                manager.edit_data()
                manager.file_manager.save_data.assert_called_once()

def test_delete_data():
    manager = TransactionManager("test_money.csv")
    with patch("builtins.input", side_effect=["1", "y"]):
        with patch.object(manager.file_manager, "load_data", return_value=[{"ID": "1", "Date": "2023-11-01 12:00:00", "Type": "Expense", "Category": "Food", "Amount": "50.0", "Description": "Lunch"}]):
            with patch.object(manager.file_manager, "save_data", MagicMock()):
                manager.delete_data()
                manager.file_manager.save_data.assert_called_once()


if __name__ == "__main__":
    main()
