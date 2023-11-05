import unittest

from utils import WWW, Git, Tweet, _, _log, hashx, mr, xmlx


class TestCase(unittest.TestCase):
    def test_init(self):
        for x in [
            WWW,
            Git,
            Tweet,
            _log,
            mr,
            hashx,
            xmlx,
            _,
        ]:
            self.assertIsNotNone(x)
