from pathlib import Path

import pandas as pd


def csv_reader(path: Path, filename: str) -> pd.DataFrame:
    """
    :param path: a class, receives directory as string
    :param filename: takes name of file
    :return: leaded dataframe from the file
    """
    full_path = path.joinpath(filename)
    _df = pd.read_csv(full_path)
    return _df
