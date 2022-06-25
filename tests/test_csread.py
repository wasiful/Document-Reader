from documentreader.csread import csv_reader
import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path


DATA_PATH = Path("tests").joinpath("datastore")


def test_csv_reader():
    expected_df = pd.DataFrame({"id": [1, 2], "mark": [20, 25]})
    actual = csv_reader(DATA_PATH, "students.csv")
    assert_frame_equal(expected_df, actual)
