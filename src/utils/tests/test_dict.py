from unittest import TestCase

from utils.Dict import Dict

TEST_DICT_RAW = dict(a=1, b=2, c=3, d=4)
TEST_DICT = Dict(TEST_DICT_RAW)


class TestDict(TestCase):
    def test_init(self):
        self.assertEqual(TEST_DICT.todict(), TEST_DICT_RAW)
        x = Dict()
        self.assertEqual(x.todict(), {})

    def test_keys(self):
        self.assertEqual(TEST_DICT.keys(), TEST_DICT_RAW.keys())

    def test_values(self):
        self.assertEqual(
            list(TEST_DICT.values()), list(TEST_DICT_RAW.values())
        )

    def test_items(self):
        self.assertEqual(TEST_DICT.items(), TEST_DICT_RAW.items())

    def test_len(self):
        self.assertEqual(TEST_DICT.len(), len(TEST_DICT_RAW))

    def test_eq(self):
        self.assertEqual(TEST_DICT, TEST_DICT_RAW)
        self.assertEqual(TEST_DICT, Dict(TEST_DICT_RAW))

    def test_getitem(self):
        for k in TEST_DICT_RAW.keys():
            self.assertEqual(TEST_DICT[k], TEST_DICT_RAW[k])

    def test_setitem(self):
        x = Dict()
        x['a'] = 11
        x['b'] = 22
        self.assertEqual(x.todict(), {'a': 11, 'b': 22})

    def test_extract_keys(self):
        self.assertEqual(TEST_DICT.extract_keys(['a']), Dict({'a': 1}))

    def test_items_sorted_by_key(self):
        self.assertEqual(
            Dict({'c': 3, 'b': 2, 'a': 1}).items_sorted_by_key(),
            [('a', 1), ('b', 2), ('c', 3)],
        )

    def test_items_sorted_by_value(self):
        self.assertEqual(
            Dict({'a': 3, 'b': 2, 'c': 1}).items_sorted_by_value(),
            [('c', 1), ('b', 2), ('a', 3)],
        )
