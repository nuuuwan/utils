"""Tests."""
import json
import unittest

from geopandas.geodataframe import GeoDataFrame
from pandas.core.frame import DataFrame
from shapely.geometry import MultiPolygon, Point

from utils import jsonx

TEST_VALUES = [
    1234,
    '1234',
    b'1234',
    {'test': 123},
    DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}),
    Point(1, 2),
    MultiPolygon(),
    GeoDataFrame(),
]


class TestJSON(unittest.TestCase):
    """Tests."""

    def test_read_and_write(self):
        """Test."""
        TEST_FILE_NAME = '/tmp/test.json'
        TEST_DATA = {'name': 'Jason', 'address': 'The Dumps'}

        jsonx.write(TEST_FILE_NAME, TEST_DATA)
        self.assertEqual(jsonx.read(TEST_FILE_NAME), TEST_DATA)

    def test_seralize_deserilize(self):
        """Test."""
        for data in TEST_VALUES:
            print(type(data))
            serlialized_data = jsonx.serialize(data)
            self.assertTrue(json.dumps(serlialized_data) is not None)
            deserialized_data = jsonx.deserialize(serlialized_data)
            self.assertEqual(str(data), str(deserialized_data))
