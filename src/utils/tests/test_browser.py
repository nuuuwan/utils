import os
from unittest import TestCase

from selenium.webdriver.common.by import By

from utils import Browser

TEST_URL = os.path.join(
    'https://nuuuwan.github.io',
    'utils',
    'data.html',
)


class TestBrowser(TestCase):
    def test_find_element_etc(self):
        browser = Browser()
        browser.open(TEST_URL)
        elem_h1 = browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('This is a test', elem_h1.text)

        elem_h1_2 = browser.find_elements(By.TAG_NAME, 'h1')[0]
        self.assertIn('This is a test', elem_h1_2.text)

        elem_h1_3 = browser.wait_for_element(By.TAG_NAME, 'h1')[0]
        self.assertIn('This is a test', elem_h1_3.text)

        browser.quit()

    def test_source(self):
        browser = Browser()
        browser.open(TEST_URL)
        self.assertIn('This is a test', browser.source)
        browser.quit()

    def test_all_others(self):
        browser = Browser()
        browser.open(TEST_URL)
        browser.set_window_dim((100, 200))
        browser.scroll_to_bottom()
        browser.sleep(1)
        browser.quit()
