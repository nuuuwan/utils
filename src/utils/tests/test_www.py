"""Test."""
import unittest
import os
from utils import www

TEST_JSON_URL = os.path.join(
    'https://raw.githubusercontent.com',
    'nuuuwan/misc-sl-data/master',
    'sl_power_station_info.json',
)

TEST_TSV_URL = os.path.join(
    'https://raw.githubusercontent.com',
    'nuuuwan/gig-data/master',
    'province.tsv',
)

TEST_INVALID_URL = 'http://www.29df.c'

TEST_IMAGE_LINK = 'https://www.python.org/static/img/python-logo@2x.png'


class testWWW(unittest.TestCase):
    """Test."""

    def test_read(self):
        """Test."""
        data = www.read(TEST_JSON_URL)
        self.assertTrue('Station' in data)

    def test_read_json(self):
        """Test."""
        data = www.read_json(TEST_JSON_URL)
        self.assertTrue('Station' in data[0])

    def test_read_tsv(self):
        """Test."""
        data = www.read_tsv(TEST_TSV_URL)
        self.assertEqual(len(data), 9)
        self.assertEqual(data[0]['province_id'], 'LK-1')

    def test_invalid_url(self):
        """Test."""
        data = www.read_json(TEST_INVALID_URL)
        self.assertEqual(data, None)

    def test_download_binary(self):
        """Test."""
        file_name = '/tmp/utils.test_www.file.png'
        www.download_binary(
            TEST_IMAGE_LINK,
            file_name,
        )
