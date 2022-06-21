import os
import unittest

from utils import Git

TEST_REPO_URL = 'https://github.com/nuuuwan/utils'
TEST_DIR_REPO = '/tmp/test.utils'


class TestCase(unittest.TestCase):
    def test_init(self):
        Git(TEST_REPO_URL)

    def test_clone(self):
        git = Git(TEST_REPO_URL)
        git.clone(TEST_DIR_REPO)
        self.assertTrue(os.path.exists(TEST_DIR_REPO))
        git.checkout('main')


if __name__ == '__main__':
    unittest.main()
