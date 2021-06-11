"""Test."""
import unittest
import time
import random
from utils.cache import cache
from utils import timex


class TestCache(unittest.TestCase):
    """Test."""

    def test_cache(self):
        """Test."""

        def func_not_cached(x):
            time.sleep(1)
            return 1

        sw = timex.StopWatch()
        x = random.random()
        func_not_cached(x)
        t_not_cached = sw.stop()

        @cache('test', 86400)
        def func_cached(x):
            return func_not_cached(x)

        x = random.random()
        func_cached(x)
        sw.reset()
        func_cached(x)
        t_cached = sw.stop()

        @cache('test', 1)
        def func_short_cached(x):
            return func_not_cached(x)

        x = random.random()
        func_short_cached(x)
        time.sleep(2)
        sw.reset()
        func_short_cached(x)
        t_short_cached = sw.stop()

        self.assertTrue(t_not_cached > 1000)
        self.assertTrue(t_cached < 100)
        self.assertTrue(t_short_cached > 1000)
