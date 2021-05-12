"""Test."""
import unittest
from utils.flask import FlaskClient


class TestFlask(unittest.TestCase):
    """Test."""

    def test_gig_server(self):
        """Test."""
        client = FlaskClient('gig', '0.0.0.0', 8080)
        self.assertEqual(
            client.run('entity', ['province', 'LK-1']),
            {
                'area': '3709',
                'capital': 'Colombo',
                'country_id': 'LK',
                'fips': 'CE36',
                'name': 'Western',
                'province_id': 'LK-1',
            },
        )
