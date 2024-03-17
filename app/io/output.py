
def write_console(data):
    """
    Print data to console

    Args:
        data (str): string to be printed
    """
    print(data)


def write_file(data, file_path):
    """
    Write data to file

    Args:
        data (str): string to be written to file
        file_path (str): path to the destination file
    """
    with open(file_path, "w") as file:
        file.write(data)


