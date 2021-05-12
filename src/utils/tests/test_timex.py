"""Test."""
import unittest
from utils import timex


class TestTime(unittest.TestCase):
    """Test."""

    def test_stop_watch(self):
        """Test."""
        sw = timex.StopWatch()
        sw.stop()
