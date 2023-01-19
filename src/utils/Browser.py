"""Browser utils."""


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import browser_firefox_profile
from utils.Log import Log

MAX_T_WAIT = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080


class Browser:
    """Browser."""

    def __init__(self):
        """Construct."""
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(
            options=options,
            firefox_profile=browser_firefox_profile.get_firefox_profile(),
        )
        self.browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.log = Log('Browser')
        self.log.debug('Opened Selenium Firefox Browser.')

    def open(self, url: str):
        self.browser.get(url)
        self.log.debug(f'Opened "{url}".')

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        SCRIPT_SCROLL = 'window.scrollTo(0, document.body.scrollHeight);'
        self.browser.execute_script(SCRIPT_SCROLL)

    @property
    def source(self):
        """Get page source."""
        return self.browser.page_source

    @property
    def downloadScreenshot(self, image_file_name):
        self.browser.save_screenshot(image_file_name)
        self.log.debug(f'Downloaded screenshot to "{image_file_name}".')

    def find_element(self, by, value):
        return self.browser.find_element(by, value)

    def quit(self):
        """Quit."""
        self.browser.close()
        self.browser.quit()
