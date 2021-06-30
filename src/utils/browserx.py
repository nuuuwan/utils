"""Browser utils."""

import time
import logging

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import filex

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('selenium-wrapper')
MAX_T_WAIT = 60
MIME_TYPES_NEVER_ASK = [
    'application/xls',
    'text/csv',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
]


class Browser:
    """Browser."""

    def __init__(self, url):
        """Construct."""
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('browser.download.folderList', 2)
        firefox_profile.set_preference(
            'browser.download.manager.showWhenStarting',
            False,
        )
        firefox_profile.set_preference('browser.download.dir', '/tmp/')
        firefox_profile.set_preference(
            'browser.helperApps.neverAsk.saveToDisk',
            ', '.join(MIME_TYPES_NEVER_ASK),
        )
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(
            options=options,
            firefox_profile=firefox_profile,
        )
        log.info('Opened "%s" in Selenium Firefox Browser', url)
        self.browser.get(url)

    def find_elements_by_id_retry(self, elem_id):
        """Find elements by id."""
        elems = None
        t_wait = 1
        while True:
            elems = self.browser.find_elements_by_id(elem_id)
            if len(elems) > 0:
                log.info('Found %d elems for id="%s"', len(elems), elem_id)
                return elems
            tmp_file = filex.get_tmp_file() + '.png'
            self.browser.save_screenshot(tmp_file)
            log.warning(
                'Could not find "%s". Waiting for %ds. Saved screenshot to %s',
                elem_id,
                t_wait,
                tmp_file,
            )
            time.sleep(t_wait)
            t_wait *= 2
            if t_wait > MAX_T_WAIT:
                log.error('Could not find any id="%s"s. Aborting', elem_id)
                return None

    def find_element_by_id_retry(self, elem_id):
        """Find single element by id."""
        elems = self.find_elements_by_id_retry(elem_id)
        if elems:
            return elems[0]
        return None

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        SCRIPT_SCROLL = 'window.scrollTo(0, document.body.scrollHeight);'
        self.browser.execute_script(SCRIPT_SCROLL)

    def scroll_to_element(self, elem):
        """Scroll to element."""
        self.browser.execute_script("arguments[0].scrollIntoView();", elem)

    def find_scroll_and_click(self, elem_id):
        """Find element, scroll to it and click."""
        elem = self.find_element_by_id_retry(elem_id)
        self.scroll_to_element(elem)
        elem.click()
        log.info('Clicked on "%s"', elem_id)
        return elem

    def get_source(self):
        """Get page source."""
        return self.browser.page_source

    def quit(self):
        """Quit."""
        self.browser.quit()
