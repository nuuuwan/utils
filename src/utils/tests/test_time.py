import time
from unittest import TestCase

from utils import (TIMEZONE_OFFSET, Time, TimeDelta, TimeFormat, get_date_id,
                   get_time_id)


class TestTime(TestCase):
    def test_init(self):
        ut = 1234567890
        t = Time(ut)
        self.assertEqual(t.ut, ut)

    def test_now(self):
        t = Time.now()
        ut = time.time()
        self.assertGreater(t.ut, ut - 10)
        self.assertGreater(ut + 10, t.ut)

    def test_sub(self):
        t0 = Time(1234567800)
        t1 = Time(1234567890)
        self.assertEqual(t1 - t0, TimeDelta(90))

    def test_add(self):
        t0 = Time(1234567800)
        dt = TimeDelta(100)
        t1 = Time(1234567900)
        self.assertEqual(t0 + dt, t1)

    def test_delta_humanize(self):
        for dut, expected_humanized in [
            [0, '0sec'],
            [1, '1sec'],
            [60, '1min'],
            [120, '2min'],
            [3600, '1hr'],
            [86400, '1day'],
        ]:
            self.assertEqual(TimeDelta(dut).humanize(), expected_humanized)

    def test_format_stringify(self):
        t = Time(1234567890)
        for format_str, expected_time_str, ut2 in [
            ['%Y-%m-%d', '2009-02-14', 1234549800],
            ['%Y-%m-%d %H:%M', '2009-02-14 05:01', 1234567860],
            ['%Y-%m-%d %H:%M:%S', '2009-02-14 05:01:30', 1234567890],
        ]:
            tf = TimeFormat(format_str, TIMEZONE_OFFSET.LK)
            self.assertEqual(
                expected_time_str,
                tf.stringify(t),
            )

            t2 = Time(ut2)
            self.assertEqual(
                t2,
                tf.parse(expected_time_str),
            )

    def test_time_id(self):
        time_id = get_time_id()
        self.assertEqual(len(time_id), 21)

    def test_date_id(self):
        date_id = get_date_id()
        self.assertEqual(len(date_id), 8)
