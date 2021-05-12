"""Tests."""
import unittest
from utils import jsonx


class TestJSON(unittest.TestCase):
    """Tests."""

    def test_read_and_write(self):
        """Test."""
        TEST_FILE_NAME = '/tmp/test.json'
        TEST_DATA = {'name': 'Jason', 'address': 'The Dumps'}

        jsonx.write(TEST_FILE_NAME, TEST_DATA)
        self.assertEqual(jsonx.read(TEST_FILE_NAME), TEST_DATA)
