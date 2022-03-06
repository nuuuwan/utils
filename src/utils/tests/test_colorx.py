"""Test."""
import random
import unittest

from utils import colorx

random.seed(0)


class TestColorX(unittest.TestCase):
    """Test."""

    def test_random_hsl_vector(self):
        self.assertEqual(
            (0.420571580830845, 1, 0.8),
            colorx.random_hsl_vector(),
        )

    def test_random_rgb_vector(self):
        self.assertEqual(
            (153, 248, 255),
            colorx.random_rgb_vector(),
        )

    def test_random_hsl(self):
        self.assertEqual(
            'hsl(1,100%,80%)',
            colorx.random_hsl(),
        )

    def test_random_rgb(self):
        self.assertEqual(
            'rgb(198,255,153)',
            colorx.random_rgb(),
        )

    def test_random_hex(self):
        self.assertEqual(
            '#ff99f8',
            colorx.random_hex(),
        )
