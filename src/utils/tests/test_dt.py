"""Test."""
import unittest

from utils import dt


class TestDT(unittest.TestCase):
    """Test."""

    def test_parse_float(self):
        """Test."""
        for [input, expected_output] in [
            ['0', 0],
            ['123', 123],
            ['123abc', None],
            ['123.456', 123.456],
        ]:
            self.assertEqual(
                dt.parse_float(input),
                expected_output,
            )

    def test_parse_int(self):
        """Test."""
        for [input, expected_output] in [
            ['0', 0],
            ['123', 123],
            ['123abc', None],
            ['123.456', None],
        ]:
            self.assertEqual(
                dt.parse_int(input),
                expected_output,
            )
