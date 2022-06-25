import os
import unittest

from utils import WWW, File

DIR_TESTS = 'src/utils/tests'
TEST_DATA_FILE = os.path.join(DIR_TESTS, 'data.txt')
TEST_HTML_FILE = os.path.join(DIR_TESTS, 'data.html')

URL_BASE = os.path.join(
    'https://raw.githubusercontent.com',
    'nuuuwan/utils',
    'main/src/utils/tests',
)
TEST_DATA_URL = os.path.join(URL_BASE, 'data.txt')
TEST_HTML_URL = os.path.join(URL_BASE, 'data.html')


class TestCase(unittest.TestCase):
    def test_read(self):
        self.assertEqual(
            File(TEST_DATA_FILE).read(),
            WWW(TEST_DATA_URL).read(),
        )

    def test_read_binary(self):
        self.assertEqual(
            File(TEST_DATA_FILE).readBinary(),
            WWW(TEST_DATA_URL).readBinary(),
        )

    def test_read_selenium(self):
        content = WWW(TEST_HTML_URL).readSelenium()
        self.assertIn(
            'This is a test',
            content,
        )


if __name__ == '__main__':
    unittest.main()
