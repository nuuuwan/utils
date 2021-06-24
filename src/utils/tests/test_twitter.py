"""Tests for utils."""

import unittest

from utils import twitter


class TestCase(unittest.TestCase):
    """Tests."""

    def test_twitter(self):
        """Test."""
        twtr = twitter.Twitter(None, None, None, None)
        self.assertEqual(twtr.tweet('Test'), False)


if __name__ == '__main__':
    unittest.main()
