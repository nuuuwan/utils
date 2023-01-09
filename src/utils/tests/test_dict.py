from unittest import TestCase

from utils import Dict

TEST_DICT = dict(a=1, b=2, c=3, d=4)
TEST_D = Dict(TEST_DICT)


class TestDict(TestCase):
    def test_init(self):
        self.assertEqual(TEST_D.d, TEST_DICT)
        d = Dict()
        self.assertEqual(d.d, {})

    def test_keys(self):
        self.assertEqual(TEST_D.keys(), TEST_DICT.keys())

    def test_values(self):
        self.assertEqual(list(TEST_D.values()), list(TEST_DICT.values()))

    def test_items(self):
        self.assertEqual(TEST_D.items(), TEST_DICT.items())

    def test_len(self):
        self.assertEqual(TEST_D.len(), len(TEST_DICT))

    def test_eq(self):
        self.assertEqual(TEST_D, TEST_DICT)
        self.assertEqual(TEST_D, Dict(TEST_DICT))

    def test_getitem(self):
        for k in TEST_DICT.keys():
            self.assertEqual(TEST_D[k], TEST_DICT[k])

    def test_setitem(self):
        d = Dict()
        d['a'] = 11
        d['b'] = 22
        self.assertEqual(d.d, {'a': 11, 'b': 22})

    def test_extract_keys(self):
        print(TEST_D.extract_keys(['a']))
        self.assertEqual(TEST_D.extract_keys(['a']), Dict({'a': 1}))

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
