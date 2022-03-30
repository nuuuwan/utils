"""Test."""
import unittest

from utils import xy

TEST_XY_LIST = [
    [0, 0],
    [4, 0],
    [0, 3],
]


class TestXY(unittest.TestCase):
    """Test."""

    def test_get_bbox(self):
        """Test."""
        actual = xy.get_bbox(TEST_XY_LIST)
        expected = [
            0, 4, 0, 3, 4, 3,
        ]
        self.assertEqual(expected, actual)

    def test_get_func_transform(self):
        """Test."""
        func_transform = xy.get_func_transform(
            WIDTH=1000, HEIGHT=500, PADDING=100, xy_list=TEST_XY_LIST)

        for input_xy, expected_output in [
            [[0, 0], [475.0, 400.0]],
            [[4, 0], [650.0, 400.0]],
            [[0, 3], [475.0, 100.0]],
        ]:
            actual_output = func_transform(input_xy)
            self.assertEqual(expected_output, actual_output)
