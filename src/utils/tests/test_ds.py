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

    def test_dict_list_get_values_for_key(self):
        """Test."""
        self.assertEqual(
            ds.dict_list_get_values_for_key(TEST_DICT_LIST, 'age'),
            ['1', '2'],
        )

    def test_get_count(self):
        int_list = [(i + 1) for i in range(0, 10000)]
        key_to_count = ds.get_count(int_list, lambda i: [i % 3])
        self.assertEqual({0: 3333, 1: 3334, 2: 3333}, key_to_count)
