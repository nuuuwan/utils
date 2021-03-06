"""Test."""
import random
import time
import unittest

import pytest
from geopandas.geodataframe import GeoDataFrame
from pandas.core.frame import DataFrame
from shapely.geometry import MultiPolygon, Point

from utils import timex
from utils.cache import cache

TEST_VALUES = [
    1234,
    '1234',
    b'1234',
    {'test': 123},
    DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}),
    Point(1, 2),
    MultiPolygon(),
    GeoDataFrame(),
]


class TestCache(unittest.TestCase):
    """Tests."""

    def test_cache_values(self):
        """Test."""
        for value in TEST_VALUES:
            random_salt = random.randint(1_000_000, 1_000_000 * 10 - 1)

            @cache('test')
            def get_value(value_dummy):
                return value

            value_nocache = get_value(random_salt)
            value_cache = get_value(random_salt)

            self.assertEqual(str(value_nocache), str(value))
            self.assertEqual(str(value_cache), str(value))

    @pytest.mark.slow
    def test_cache_speed(self):
        """Test."""

        def func_not_cached(x):
            time.sleep(1)
            return 1

        sw = timex.StopWatch()
        x = random.random()
        func_not_cached(x)
        t_not_cached = sw.stop()

        @cache('test')
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
