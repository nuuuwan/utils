"""Utils for reading remote files."""
import os
import ssl

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import hashx
from utils.file.CSVFile import CSVFile
from utils.file.File import File
from utils.file.JSONFile import JSONFile
from utils.file.TSVFile import TSVFile
from utils.Log import Log

log = Log('WWW')

USER_AGENT = ''.join(
    [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) ',
        'Gecko/20100101 Firefox/65.0',
    ]
)

ENCODING = 'utf-8'
SELENIUM_SCROLL_REPEATS = 3
SELENIUM_SCROLL_WAIT_TIME = 0.5
EXISTS_TIMEOUT = 1

HASH_LENGTH = 8

BINARY_EXT_LIST = ['pdf', 'png', 'jpg', 'jpeg']
NON_BINARY_EXT_LIST = ['json', 'tsv', 'csv', 'txt']
HTML_EXT_LIST = ['htm', 'html']
CUSTOM_EXT_LIST = BINARY_EXT_LIST + NON_BINARY_EXT_LIST

# pylint: disable=W0212
ssl._create_default_https_context = ssl._create_unverified_context


class WWW:
    def __init__(self, url: str):
        self.url = url

    @property
    def hash_id(self):
        return hashx.md5(self.url)[:HASH_LENGTH]

    @property
    def ext(self):
        ext = 'htm'
        for ext2 in CUSTOM_EXT_LIST + HTML_EXT_LIST:
            if self.url.endswith(ext2):
                ext = ext2
                break
        return ext

    @property
    def local_path(self):
        return os.path.join('/tmp', f'www.{self.hash_id}.{self.ext}')

    def read_html(self):
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.get(self.url)
        content = driver.page_source
        driver.quit()
        return content

    def download_html(self):
        html = self.read_html()
        File(self.local_path).write(html)
        return self.local_path

    def download_binary(self, file_path):
        os.system(f'wget -o "{file_path}" "{self.url}"')
        log.debug(f'Downloaded {self.url} to {file_path}')
        return self.local_path

    def download(self):
        if os.path.exists(self.local_path):
            return self.local_path

        if not self.exists:
            raise Exception(f'WWW does not exist: {self.url}')

        if self.ext in HTML_EXT_LIST:
            return self.download_html()
        return self.download_binary(self.local_path)

    def read(self):
        self.download()
        if self.ext in NON_BINARY_EXT_LIST:
            return File(self.local_path).read()
        return File(self.local_path).readBinary()

    @property
    def exists(self):
        try:
            response = requests.head(self.url, timeout=EXISTS_TIMEOUT)
            # pylint: disable=E1101
            return response.status_code == requests.codes.ok
        except requests.exceptions.ConnectTimeout:
            return False

    @property
    def children(self):
        soup = self.soup
        if not soup:
            return []
        links = soup.find_all('a')
        raw_urls = [WWW(link.get('href')) for link in links]
        raw_urls = list(filter(lambda x: x.url, raw_urls))
        return list(sorted(set(raw_urls), key=lambda x: x.url))

    @property
    def soup(self):
        if self.ext != 'htm':
            return None
        return BeautifulSoup(self.read(), 'html.parser')

    # -----------
    # Legacy methods (should be deprecated)
    # -----------
    def readJSON(self):
        return JSONFile(self.download()).read()

    def readTSV(self):
        return TSVFile(self.download()).read()

    def readCSV(self):
        return CSVFile(self.download()).read()

    def readBinary(self):
        return File(self.download()).readBinary()

    def readSelenium(self):
        return self.read_html()
