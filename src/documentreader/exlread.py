import pandas as pd
from pathlib import Path


def excel_reader(path: Path, filename: str):
    """
    :param path: a class, receives directory as string
    :param filename: takes name of file
    :return: leaded dataframe from the file
    """
    file_path = path.joinpath(filename)    # providing the file name
    df = pd.read_excel(file_path)   # loading the data frame using the directory
    return df
