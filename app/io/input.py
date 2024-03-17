import pandas as pd


def read_console():
    """
    Read input from console

    Returns:
        str: input from console
    """
    return input()


def read_file(file_path):
    """
    Read input from file

    Args:
        file_path(str): input file path

    Returns:
        str: input from file
    """
    with open(file_path) as file:
        result = file.read()
    return result


def read_file_pandas(file_path):
    """
    Read input from file using pandas

    Args:
        file_path(str): input file path

    Returns:
        str: input from file

    """
    return pd.read_csv(file_path).to_csv()
