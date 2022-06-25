import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path

from documentreader.jsread import json_reader

DATA_PATH = Path("tests").joinpath("datastore")


def test_json_reader():
    expected = pd.DataFrame(
        [["a", "b"], ["c", "d"]], index=["row 1", "row 2"], columns=["col 1", "col 2"]
    )
    actual = json_reader(DATA_PATH, "dummy.json", orient="split")
    assert_frame_equal(expected, actual)
