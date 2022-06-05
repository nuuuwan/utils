
import unittest

from utils import GoogleMaps

TEST_ADDRESS_AND_LATLNG = [
    [
        'WV87+7CW, Dr CWW Kannangara Mawatha, Colombo 00700, Sri Lanka',
        [6.9157375, 79.8635781],
    ],
    [
        '101 Kumaratunga Munidasa Mawatha, Colombo 00700, Sri Lanka',
        [6.8994025, 79.8600437],
    ],
    [
        '54 Chatham St, Colombo 00100, Sri Lanka',
        [6.9344566, 79.8430699],
    ]
]


class TestCase(unittest.TestCase):
    def test_get_address(self):
        google_maps = GoogleMaps()
        for expected_address, latlng in TEST_ADDRESS_AND_LATLNG:
            actual_address = google_maps.get_address(latlng)
            self.assertEqual(expected_address, actual_address)

    def test_get_latlng(self):
        google_maps = GoogleMaps()
        for address, expected_latlng in TEST_ADDRESS_AND_LATLNG:
            actual_latlng = google_maps.get_latlng(address)
            self.assertAlmostEqual(expected_latlng[0], actual_latlng[0])
            self.assertAlmostEqual(expected_latlng[1], actual_latlng[1])


if __name__ == '__main__':
    unittest.main()
