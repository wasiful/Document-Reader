import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path

# from the exlread main file using the reader function
from documentreader.exlread import excel_reader

# joins directory folders and sub folders to create path in any OS
GIVEN_PATH = Path("tests").joinpath("datastore")


def test_excel_reader():
    # giving similar data to test.
    expected_df = pd.DataFrame(
        {"product": ["apple", "orange", "banana"], "amount": [20, 30, 40]}
    )
    # the function receives file name, reads the data, loads it for assertion
    actual_df = excel_reader(GIVEN_PATH, "dummy.xlsx")
    # comparing both data if equal or not
    assert_frame_equal(expected_df, actual_df)
