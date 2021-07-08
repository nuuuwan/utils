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

    def test_get_area(self):
        """Test."""
        latlng_list_list = [
            [
                [79.88103657474609, 6.773556777772627],
                [79.84936944177436, 6.938697429248654],
                [80.1895235454997, 6.976344734804433],
                [80.18457380299158, 6.815202975465847],
                [79.88103657474609, 6.773556777772627],
            ]
        ]
        self.assertEqual(geo.get_area(latlng_list_list), 652.4958132934988)
