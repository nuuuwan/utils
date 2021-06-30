"""Tests for hashx"""

import os
import unittest

from utils.browserx import Browser

TEST_URL = os.path.join(
    'https://github.com/nuuuwan',
    'utils/blob/main/src/utils/tests/TestData.xls',
)


class TestBrowserX(unittest.TestCase):
    """Tests."""

    def test_browser(self):
        """Test."""
        os.system('rm -rf /tmp/TestData.xls')
        browser = Browser(TEST_URL)
        self.assertTrue(browser is not None)
        browser.find_scroll_and_click('raw-url')
        browser.scroll_to_bottom()
        self.assertTrue(browser.wait_and_quit('/tmp/TestData.xls') is not None)


if __name__ == '__main__':
    unittest.main()
