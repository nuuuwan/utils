"""Test."""
import unittest

from utils.latlng import Bounds, LatLng, LatLngIndex, Polygon


class TestLatLng(unittest.TestCase):
    """Test."""

    def test_str(self):
        """Test."""
        latlng = LatLng(7, 81)
        self.assertEqual('(7.000000, 81.000000)', str(latlng))

    def test_distance(self):
        """Test."""
        latlng1 = LatLngIndex.DONDRA_HEAD
        latlng2 = LatLngIndex.POINT_PEDRO

        actual_distance = latlng1.distance(latlng2)
        self.assertAlmostEqual(437.132, actual_distance, places=3)

    def test_bounds(self):
        latlng = LatLng(7, 81)
        self.assertEqual(Bounds(LatLng(7, 81), LatLng(7, 81)), latlng.bounds)

    def test_polygon_len(self):
        polygon = Polygon(
            [
                LatLngIndex.DONDRA_HEAD,
                LatLngIndex.SANGAMAN_KANDA,
                LatLngIndex.POINT_PEDRO,
                LatLngIndex.KANCHCHATHEEVU,
                LatLngIndex.DONDRA_HEAD,
            ]
        )
        self.assertEqual(5, len(polygon))

    def test_polygon_bounds(self):
        polygon = Polygon(
            [
                LatLngIndex.DONDRA_HEAD,
                LatLngIndex.SANGAMAN_KANDA,
                LatLngIndex.POINT_PEDRO,
                LatLngIndex.KANCHCHATHEEVU,
                LatLngIndex.DONDRA_HEAD,
            ]
        )
        print(polygon.bounds)
        self.assertEqual(
            Bounds(
                LatLng(5.923389, 79.516667),
                LatLng(9.835556, 81.879167),
            ),
            polygon.bounds,
        )
