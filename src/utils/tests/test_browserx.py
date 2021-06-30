"""Tests for hashx"""

import unittest

from utils.browserx import Browser


class TestBrowserX(unittest.TestCase):
    """Tests."""

    def test_browser(self):
        """Test."""
        browser = Browser('https://www.python.org/')
        self.assertTrue(browser is not None)
        browser.scroll_to_bottom()


if __name__ == '__main__':
    unittest.main()
