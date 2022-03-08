"""Test."""
import unittest

from utils import timex

PARSE_FORMAT_TEST_CASES = [
    [
        '2021-01-01',
        '%Y-%m-%d',
        timex.TIMEZONE_OFFSET_LK,
        1_609_439_400,
    ],
    [
        '2021-01-01',
        '%Y-%m-%d',
        timex.TIMEZONE_OFFSET_GMT,
        1_609_439_400 + 19_800,
    ],
    [
        '2021-01-01 12:34:56',
        '%Y-%m-%d %H:%M:%S',
        timex.TIMEZONE_OFFSET_LK,
        1_609_484_696,
    ],
    [
        'April 01, 2020',
        '%B %d, %Y',
        timex.TIMEZONE_OFFSET_LK,
        1_585_679_400,
    ],
    [
        'February 29, 2021',
        '%B %d, %Y',
        timex.TIMEZONE_OFFSET_LK,
        None,
    ],
]


class TestTime(unittest.TestCase):
    """Test."""

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
        for [
            time_str,
            time_format,
            timezone,
            expected_unixtime,
        ] in PARSE_FORMAT_TEST_CASES:
            if expected_unixtime:
                self.assertEqual(
                    expected_unixtime,
                    timex.parse_time(time_str, time_format, timezone),
                )
            else:
                with self.assertRaises(ValueError):
                    timex.parse_time(time_str, time_format, timezone)

    def test_format_time(self):
        """Test."""
        for [
            expected_time_str,
            time_format,
            timezone,
            unixtime,
        ] in PARSE_FORMAT_TEST_CASES:
            if unixtime:
                self.assertEqual(
                    expected_time_str,
                    timex.format_time(unixtime, time_format, timezone),
                )

    def test_seconds_in(self):
        """Test."""
        self.assertEqual(timex.SECONDS_IN.HOUR, 3600)
        self.assertEqual(timex.SECONDS_IN.DAY, 86400)
        self.assertEqual(timex.SECONDS_IN.YEAR, 31557600)
