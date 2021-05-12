"""Test."""
import unittest
from utils.ds import dict_list_to_index

TEST_DICT_LIST = [
    {'name': 'Alpha', 'age': '1'},
    {'name': 'Bravo', 'age': '2'},
]


class TestDS(unittest.TestCase):
    """Test."""

    def test_dict_list_to_index(self):
        """Test."""
        self.assertEqual(
            {
                'Alpha': {'name': 'Alpha', 'age': '1'},
                'Bravo': {'name': 'Bravo', 'age': '2'},
            },
            dict_list_to_index(TEST_DICT_LIST, 'name'),
        )
