from pathlib import Path

import pandas as pd


def json_reader(path: Path, filename: str, orient: str) -> pd.DataFrame:
    """
    :param path: a class, receives directory as string
    :param filename: takes name of file
    :param orient: sorts dataframe, controls the orientation of the data frame
    :return: leaded dataframe from the file
    """
    filepath = path.joinpath(filename)
    _df = pd.read_json(filepath, orient=orient)
    return _df
