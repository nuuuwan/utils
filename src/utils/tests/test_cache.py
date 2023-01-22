from unittest import TestCase

from utils import SECONDS_IN, cache

TIMEOUT = SECONDS_IN.MINUTE


class TestCache(TestCase):
    def test_simple(self):
        @cache('test_simple', TIMEOUT)
        def inner():
            return 1

        self.assertEqual(inner(), 1)

    def test_with_params(self):
        @cache('test_simple', TIMEOUT)
        def inner(x):
            return x

        x_list = (
            [y for y in range(0, 10)]
            + [dict(a=1, b=2)]
            + ['a', 'b', 'c']
            + [None]
        )
        for x in x_list:
            self.assertEqual(inner(x), x)
