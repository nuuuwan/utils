"""Test."""
import random
import unittest

from utils import colorx


class TestColorX(unittest.TestCase):
    """Test."""

    def test_random_hsl_vector(self):
        random.seed(0)
        self.assertEqual(
            (0.84, 1, 0.8),
            colorx.random_hsl_vector(),
        )

        self.assertEqual(
            (0.5, 0.6, 0.7),
            colorx.random_hsl_vector(hue=0.5, saturation=0.6, lightness=0.7),
        )

        self.assertEqual(
            (0.42, 0.6, 0.7),
            colorx.random_hsl_vector(saturation=0.6, lightness=0.7),
        )

        self.assertEqual(
            (0.26, 1, 0.7),
            colorx.random_hsl_vector(lightness=0.7),
        )

    def test_random_rgb_vector(self):
        random.seed(1)
        self.assertEqual(
            (255, 232, 153),
            colorx.random_rgb_vector(),
        )

        self.assertEqual(
            (100, 120, 130),
            colorx.random_rgb_vector(red=100, green=120, blue=130),
        )

        self.assertEqual(
            (210, 120, 130),
            colorx.random_rgb_vector(green=120, blue=130),
        )

        self.assertEqual(
            (197, 255, 130),
            colorx.random_rgb_vector(blue=130),
        )

    def test_random_hsl(self):
        random.seed(2)
        self.assertEqual(
            'hsl(1,100%,80%)',
            colorx.random_hsl(),
        )

        self.assertEqual(
            'hsl(1,80%,80%)',
            colorx.random_hsl(saturation=0.8),
        )

    def test_random_rgb(self):
        random.seed(3)
        self.assertEqual(
            'rgb(210,255,153)',
            colorx.random_rgb(),
        )
        self.assertEqual(
            'rgb(153,230,100)',
            colorx.random_rgb(blue=100),
        )

    def test_random_hex(self):
        random.seed(4)
        self.assertEqual(
            '#d2ff99',
            colorx.random_hex(),
        )
        self.assertEqual(
            'rgb(255,214,253)',
            colorx.random_rgb(blue=253),
        )
