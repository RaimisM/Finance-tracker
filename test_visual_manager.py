import pytest
import os
import pandas as pd
from visual_manager import VisualManager

def main():
    test_load_data()
    test_get_file_modification_time()
    test_filter_data_month()

def test_load_data():
    visual_manager = VisualManager("test_money.csv")
    assert not visual_manager.data.empty
    assert len(visual_manager.data) == 3

def test_get_file_modification_time():
    visual_manager = VisualManager("test_money.csv")
    mod_time = visual_manager.get_file_modification_time()
    assert mod_time is not None
    assert isinstance(mod_time, float)

def test_filter_data_month():
    visual_manager = VisualManager("test_money.csv")
    filtered_data = visual_manager.filter_data("month")
    assert not filtered_data.empty
    assert filtered_data["Date"].dt.month.iloc[0] == 12


if __name__ == "__main__":
    main()
