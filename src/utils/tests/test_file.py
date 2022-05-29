
import unittest

from utils import CSVFile, File, JSONFile, TSVFile

TEST_DATA_LIST = [
    {'name': 'Alpha', 'age': '1'},
    {'name': 'Bravo', 'age': '2'},
]

TEST_DATA_ITEM_LIST = [
    True,
    1234,
    1234.5678,
    '1234',
    [1, 2, 3, 'test'],
    {'test': 123},
    TEST_DATA_LIST,
]


class TestCase(unittest.TestCase):
    def test_read_and_write(self):
        """Test."""
        content = 'Hello' * 100
        file = File('/tmp/utils.test_file.txt')
        file.write(content)
        content2 = file.read()
        self.assertEqual(content, content2)

    def test_json_read_and_write(self):
        for data in TEST_DATA_ITEM_LIST:
            json_file = JSONFile('/tmp/utils.test_file.json')
            json_file.write(data)
            data2 = json_file.read()
            self.assertEqual(data, data2)

    def test_csv_read_and_write(self):
        csv_file = CSVFile('/tmp/utils.test_file.csv')
        csv_file.write(TEST_DATA_LIST)
        data_list = csv_file.read()
        self.assertEqual(TEST_DATA_LIST, data_list)

    def test_tsv_read_and_write(self):
        tsv_file = TSVFile('/tmp/utils.test_file.tsv')
        tsv_file.write(TEST_DATA_LIST)
        data_list = tsv_file.read()
        self.assertEqual(TEST_DATA_LIST, data_list)


if __name__ == '__main__':
    unittest.main()
