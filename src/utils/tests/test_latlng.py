"""Test."""
import unittest

from utils.latlng import LatLng


class TestLatLng(unittest.TestCase):
    """Test."""

    def test_str(self):
        """Test."""
        latlng = LatLng(7, 81)
        self.assertEqual('(7.000000, 81.000000)', str(latlng))

    def test_distance(self):
        """Test."""
        latlng1 = LatLng(6.940153, 79.878257)
        latlng2 = LatLng(6.892342, 79.877043)

        actual_distance = latlng1.distance(latlng2)
        self.assertAlmostEqual(5.320, actual_distance, places=3)
