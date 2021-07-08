"""Test."""
import unittest

from utils import ds

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
            ds.dict_list_to_index(TEST_DICT_LIST, 'name'),
        )

    def test_sort_dict_items_by_key(self):
        """Test."""
        self.assertEqual(
            [
                ('one', 1),
                ('three', 3),
                ('two', 2),
            ],
            ds.sort_dict_items_by_key(
                {
                    'one': 1,
                    'two': 2,
                    'three': 3,
                }
            ),
        )
