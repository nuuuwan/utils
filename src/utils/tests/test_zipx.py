"""Test."""
import io
import os
import unittest

from utils.zipx import download_zip, unzip


class TestZipX(unittest.TestCase):
    """Test."""

    def test_download_and_unzip(self):
        os.system('rm -rf /tmp/utils.test_zipx*')

        url_download = os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/utils/main',
            'src/utils/tests/test_zipx_example1.txt.zip ',
        )
        zip_file = '/tmp/utils.test_zipx_example1.zip'
        download_zip(url_download, zip_file)

        dir_unzip = os.path.join('/tmp/test_zipx_example1')
        unzip(zip_file, dir_unzip)
        actual_txt_file = os.path.join(dir_unzip, 'test_zipx_example1.txt')
        expected_txt_file = 'src/utils/tests/test_zipx_example1.txt'

        self.assertListEqual(
            list(io.open(actual_txt_file)),
            list(io.open(expected_txt_file)),
        )
