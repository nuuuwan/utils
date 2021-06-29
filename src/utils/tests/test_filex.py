"""Tests for filex"""

import unittest

from utils import filex


class TestFilex(unittest.TestCase):
    """Tests."""

    def test_read_and_write(self):
        """Test."""
        content = 'Hello' * 100
        file_name = '/tmp/utils.test_filex.txt'
        filex.write(file_name, content)
        content2 = filex.read(file_name)
        self.assertEqual(content, content2)

    def test_get_tmp_file(self):
        """Test."""
        tmp_file = filex.get_tmp_file()
        self.assertEqual(len(tmp_file), 40)
        tmp_file2 = filex.get_tmp_file()
        self.assertTrue(tmp_file != tmp_file2)


if __name__ == '__main__':
    unittest.main()
