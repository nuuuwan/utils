"""Test."""
import unittest
import time
from utils import timex

TIMEZONE_OFFSET_LK = 19800


class TestTime(unittest.TestCase):
    """Test."""

    def test_stop_watch(self):
        """Test."""
        sw = timex.StopWatch()
        sw.stop()

    def test_get_unixtime(self):
        """Test."""
        ut = timex.get_unixtime()
        self.assertIsInstance(ut, int)
        self.assertTrue(ut > 1_600_000_000)

    def test_parse_time(self):
        """Test."""
        timezone_offset = (TIMEZONE_OFFSET_LK + time.timezone)
        for [time_str, time_format, expected_unixtime] in [
            ['2021-01-01', '%Y-%m-%d', 1_609_439_400],
            ['2021-01-01 12:34:56', '%Y-%m-%d %H:%M:%S', 1_609_484_696],
            ['April 1, 2020', '%B %d, %Y', 1_585_679_400],
            ['February 29, 2021', '%B %d, %Y', None],
        ]:
            if expected_unixtime:
                self.assertEqual(
                    expected_unixtime + timezone_offset,
                    timex.parse_time(time_str, time_format),
                )
            else:
                with self.assertRaises(ValueError):
                    timex.parse_time(time_str, time_format)
