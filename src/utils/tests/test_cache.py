"""Test."""
import unittest
import time
import random
from utils.cache import cache, _json_serialize, _json_deserialize
from utils import timex


class TestCache(unittest.TestCase):
    """Tests."""

    def test_json_serialize_deserialize(self):
        """Test."""
        for data in [
            1234,
            '1234',
            b'1234',
        ]:
            serlialized_data = _json_serialize(data)
            deserialized_data = _json_deserialize(serlialized_data)
            self.assertEqual(data, deserialized_data)

    def test_cache_values(self):
        """Test."""
        random_salt = random.randint(1_000_000, 1_000_000 * 10 - 1)
        random_int = random.randint(1_000_000, 1_000_000 * 10 - 1)
        random_bytes = b'%d' % (random_int)

        for value in [random_bytes]:

            @cache('test')
            def get_random_int(value_dummy):
                return value

            value_nocache = get_random_int(random_salt)
            value_cache = get_random_int(random_salt)

            self.assertEqual(value_nocache, value)
            self.assertEqual(value_cache, value)

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
