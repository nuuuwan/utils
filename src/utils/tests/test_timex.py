"""Test."""
import unittest
import time
from utils import timex

TIMEZONE_OFFSET_LK = 19800
PARSE_FORMAT_TEST_CASES = [
    ['2021-01-01', '%Y-%m-%d', 1_609_439_400],
    ['2021-01-01 12:34:56', '%Y-%m-%d %H:%M:%S', 1_609_484_696],
    ['April 01, 2020', '%B %d, %Y', 1_585_679_400],
    ['February 29, 2021', '%B %d, %Y', None],
]


class TestTime(unittest.TestCase):
    """Test."""

    def test_stop_watch(self):
        """Test."""
        stopwatch = timex.StopWatch()
        time.sleep(1)
        delta_t = stopwatch.stop()
        self.assertTrue(1000 < delta_t < 1100)

    def test_get_timezone(self):
        """Test."""
        timezone = timex.get_timezone()
        self.assertIn(timezone, ['+0530', 'UTC'])

    def test_get_unixtime(self):
        """Test."""
        unixtime = timex.get_unixtime()
        self.assertIsInstance(unixtime, int)
        self.assertTrue(unixtime > 1_600_000_000)

    def test_parse_time(self):
        """Test."""
        timezone_offset = (TIMEZONE_OFFSET_LK + time.timezone)
        for [time_str, time_format, expected_unixtime] \
                in PARSE_FORMAT_TEST_CASES:
            if expected_unixtime:
                self.assertEqual(
                    expected_unixtime + timezone_offset,
                    timex.parse_time(time_str, time_format),
                )
            else:
                with self.assertRaises(ValueError):
                    timex.parse_time(time_str, time_format)

    def test_format_time(self):
        """Test."""
        timezone_offset = (TIMEZONE_OFFSET_LK + time.timezone)
        for [expected_time_str, time_format, unixtime] \
                in PARSE_FORMAT_TEST_CASES:
            if unixtime:
                self.assertEqual(
                    expected_time_str,
                    timex.format_time(unixtime + timezone_offset, time_format),
                )

    def test_seconds_in(self):
        """Test."""
        self.assertEqual(timex.SECONDS_IN.HOUR, 3600)
        self.assertEqual(timex.SECONDS_IN.DAY, 86400)
        self.assertEqual(timex.SECONDS_IN.YEAR, 31557600)
