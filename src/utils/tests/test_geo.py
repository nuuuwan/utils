"""Test."""
import unittest
from utils import geo


class TestGeo(unittest.TestCase):
    """Test."""

    def test_get_distance(self):
        """Test."""
        latlng1 = [7, 80]
        latlng2 = [8, 80]
        latlng3 = [9, 80]

        self.assertEqual(
            geo.get_distance(latlng1, latlng1),
            0,
        )
        self.assertEqual(
            geo.get_distance(latlng1, latlng2),
            geo.get_distance(latlng2, latlng3),
        )

    def test_parse_latlng(self):
        """Test."""
        for [latlng_str, expected_latlng] in [
            ['6.9271° N, 79.8612° E', (6.9271, 79.8612)],
            ['6.9271N,79.8612E', (6.9271, 79.8612)],
            ['6.9271,79.8612', (6.9271, 79.8612)],
        ]:
            self.assertEqual(
                expected_latlng,
                geo.parse_latlng(latlng_str),
            )
