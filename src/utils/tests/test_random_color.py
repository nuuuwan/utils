"""Test."""
import random
import unittest

from utils.RandomColor import RandomColor


class TestColorX(unittest.TestCase):
    """Test."""

    def test_8bit(self):
        random.seed(0)
        self.assertEqual(RandomColor._8bit(), 197)

    def test_360(self):
        random.seed(0)
        self.assertAlmostEqual(RandomColor._360(), 197)

    def test_float(self):
        random.seed(0)
        self.assertAlmostEqual(RandomColor._float(), 0.8444218515250481)

    def test_percent(self):
        random.seed(0)
        self.assertAlmostEqual(RandomColor._percent(), 49)

    def test_rgb(self):
        random.seed(0)
        self.assertEqual(RandomColor.rgb(), 'rgba(197,215,20,0.26)')

    def test_hsla(self):
        random.seed(0)
        self.assertEqual(RandomColor.hsla(), 'hsla(197,97%,53%,0.04)')
