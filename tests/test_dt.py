"""Test."""
import unittest

from utils import dt

SNAKE_AND_CAMEL_EXAMPLES = [
    ['this_is_a_test', 'ThisIsATest'],
    ['123', '123'],
    ['123_testing123', '123Testing123'],
]


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
            ['123.456', 123],
        ]:
            self.assertEqual(
                dt.parse_int(input),
                expected_output,
            )

    def test_to_snake(self):
        """Test."""
        for [input, expected_output] in [
            ['This is a test', 'this_is_a_test'],
            ['123', '123'],
            ['123 Testing 123', '123_testing_123'],
        ]:
            self.assertEqual(
                dt.to_snake(input),
                expected_output,
            )

    def test_to_kebab(self):
        """Test."""
        for [input, expected_output] in [
            ['This is a test', 'this-is-a-test'],
            ['123', '123'],
            ['123 Testing 123', '123-testing-123'],
        ]:
            self.assertEqual(
                dt.to_kebab(input),
                expected_output,
            )

    def test_snake_to_camel(self):
        for [input, expected_output] in SNAKE_AND_CAMEL_EXAMPLES:
            self.assertEqual(
                dt.snake_to_camel(input),
                expected_output,
            )

    def test_camel_to_snake(self):
        for [expected_output, input] in SNAKE_AND_CAMEL_EXAMPLES:
            self.assertEqual(
                dt.camel_to_snake(input),
                expected_output,
            )
