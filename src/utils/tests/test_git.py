import os
import unittest

from utils import Git

TEST_REPO_URL = 'https://github.com/nuuuwan/utils'
TEST_DIR_REPO = '/tmp/test.utils'
TEST_BRACH_NAME = 'main'


class TestCase(unittest.TestCase):
    def test_init(self):
        Git(TEST_REPO_URL)

    def test_clone(self):
        git = Git(TEST_REPO_URL)
        git.clone(TEST_DIR_REPO, force=True)
        git.checkout(TEST_BRACH_NAME)
        self.assertTrue(os.path.exists(TEST_DIR_REPO))


if __name__ == '__main__':
    unittest.main()
