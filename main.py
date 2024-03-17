from app.io.input import read_console, read_file, read_file_pandas
from app.io.output import write_console, write_file


def main():
    result_console = read_console()
    write_console(result_console)
    write_file(result_console, "./data/out/read_console.csv")

    result_file = read_file("./data/in/test_data.csv")
    write_console(result_file)
    write_file(result_file, "./data/out/read_file.csv")

    result_pandas = read_file_pandas("./data/in/test_data.csv")
    write_console(result_pandas)
    write_file(result_pandas, "./data/out/result_pandas.csv")


if __name__ == '__main__':
    main()