"""Test."""
import io
import os
import unittest

from utils.zipx import download_zip, unzip


class TestZipX(unittest.TestCase):
    """Test."""

    def test_download_and_unzip(self):
        url_download = os.path.join(
            'https://github.com',
            'nuuuwan/utils',
            'blob/main/src/utils/tests/test_zipx_example1.txt.zip?raw=true',
        )
        zip_file = '/tmp/utils.test_zipx_example1_actual.txt.zip'
        download_zip(url_download, zip_file)

        actual_txt_file = os.path.join(
            '/tmp/utils.test_zipx_example1_actual.txt',
            'test_zipx_example1.txt'
        )
        unzip(zip_file, actual_txt_file)

        expected_txt_file = 'src/utils/tests/test_zipx_example1.txt'

        self.assertListEqual(
            list(io.open(actual_txt_file)),
            list(io.open(expected_txt_file)),
        )
