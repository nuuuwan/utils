import unittest

from utils.GoogleMaps import GoogleMaps

SKIP_API_KEY = 'Needs GoogleMaps API Key'

TEST_ADDRESS_AND_LATLNG_DETAILS = [
    [
        'WV87+7CW, Dr CWW Kannangara Mawatha, Colombo 00700, Sri Lanka',
        [6.9157375, 79.8635781],
        {
            'street_number': None,
            'plus_code': 'WV87+7CW',
            'street': 'Doctor CWW Kannangara Mawatha',
            'sub_city': 'Cinnamon Gardens',
            'city': 'Colombo',
            'postal_code': '00700',
            'district': 'Colombo',
            'province': 'Western Province',
            'country': 'Sri Lanka',
            'formatted_address': 'WV87+7CW, Dr CWW Kannangara Mawatha,'
            + ' Colombo 00700, Sri Lanka',
        },
    ],
    [
        '101 Kumaratunga Munidasa Mawatha, Colombo 00700, Sri Lanka',
        [6.8994025, 79.8600437],
        {
            'street_number': '101',
            'plus_code': None,
            'street': 'Kumaratunga Munidasa Mawatha',
            'sub_city': None,
            'city': 'Colombo',
            'postal_code': '00700',
            'district': 'Colombo',
            'province': 'Western Province',
            'country': 'Sri Lanka',
            'formatted_address': '101 Kumaratunga Munidasa Mawatha,'
            + ' Colombo 00700, Sri Lanka',
        },
    ],
    [
        '54 Chatham St, Colombo 00100, Sri Lanka',
        [6.9344566, 79.8430699],
        {
            'street_number': '54',
            'plus_code': None,
            'street': 'Chatham Street',
            'sub_city': 'Colombo 01',
            'city': 'Colombo',
            'postal_code': '00100',
            'district': 'Colombo',
            'province': 'Western Province',
            'country': 'Sri Lanka',
            'formatted_address': '54 Chatham St, Colombo 00100,'
            + ' Sri Lanka',
        },
    ],
    [
        '42 Sangaraja Mawatha, Kandy 20000, Sri Lanka',
        [7.291622, 80.6424206],
        {
            'street_number': '42',
            'plus_code': None,
            'street': 'Sangaraja Mawatha',
            'sub_city': None,
            'city': 'Kandy',
            'postal_code': '20000',
            'district': 'Kandy',
            'province': 'Central Province',
            'country': 'Sri Lanka',
            'formatted_address': '42 Sangaraja Mawatha, Kandy 20000,'
            + ' Sri Lanka',
        },
    ],
]


class TestCase(unittest.TestCase):
    @unittest.skip(SKIP_API_KEY)
    def test_get_latlng(self):
        google_maps = GoogleMaps()
        for address, expected_latlng, __ in TEST_ADDRESS_AND_LATLNG_DETAILS:
            actual_latlng = google_maps.get_latlng(address)
            self.assertAlmostEqual(expected_latlng[0], actual_latlng[0])
            self.assertAlmostEqual(expected_latlng[1], actual_latlng[1])

    @unittest.skip(SKIP_API_KEY)
    def test_get_address(self):
        google_maps = GoogleMaps()
        for expected_address, latlng, __ in TEST_ADDRESS_AND_LATLNG_DETAILS:
            actual_address = google_maps.get_address(latlng)
            self.assertEqual(expected_address, actual_address)

    @unittest.skip(SKIP_API_KEY)
    def test_get_address_details(self):
        google_maps = GoogleMaps()
        for __, latlng, expected_details in TEST_ADDRESS_AND_LATLNG_DETAILS:
            print(latlng, expected_details)
            actual_details = google_maps.get_address_details(latlng)
            self.assertEqual(expected_details, actual_details)
