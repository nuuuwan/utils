import unittest

from utils import (
    TTS,
    WWW,
    Git,
    Image,
    LatLng,
    Translator,
    Tweet,
    _,
    _log,
    hashx,
    mr,
    xmlx,
)


class TestCase(unittest.TestCase):
    def test_init(self):
        for x in [
            WWW,
            Git,
            Tweet,
            _,
            _log,
            hashx,
            mr,
            xmlx,
            Image,
            LatLng,
            Translator,
            TTS,
        ]:
            self.assertIsNotNone(x)
