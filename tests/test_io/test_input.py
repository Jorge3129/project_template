import unittest
from app.io.input import read_file, read_file_pandas


class TestInputFunctions(unittest.TestCase):
    def test_read_file_success(self):
        result = read_file("./data/in/test_data.csv")
        self.assertEqual(result, "1, 2, 3")

    def test_read_file_fail(self):
        with self.assertRaises(FileNotFoundError):
            read_file("./data/in/test_data1.csv")

    def test_read_file_empty_success(self):
        result = read_file("./data/in/empty.csv")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
