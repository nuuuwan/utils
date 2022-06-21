"""Tests for utils."""

import unittest

from utils import twitter

SKIP_API_CREDENTIALS = 'Needs Twitter API credentials'


class TestCase(unittest.TestCase):
    """Tests."""

    @unittest.skip(SKIP_API_CREDENTIALS)
    def test_twitter(self):
        """Test."""
        twtr = twitter.Twitter(None, None, None, None)
        self.assertEqual(twtr.tweet('Test'), None)


if __name__ == '__main__':
    unittest.main()
