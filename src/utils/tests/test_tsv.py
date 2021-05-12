"""Test."""
import unittest
from utils import tsv

from test_ds import TEST_DICT_LIST


class TestTSV(unittest.TestCase):
    """Test."""

    def test_read_and_write(self):
        """Test."""
        file_name = '/tmp/test.tsv'
        tsv.write(file_name, TEST_DICT_LIST)
        dict_list = tsv.read(file_name)
        self.assertEqual(TEST_DICT_LIST, dict_list)
