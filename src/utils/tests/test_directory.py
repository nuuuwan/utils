from unittest import TestCase

from utils import Directory, File


class TestDirectory(TestCase):
    def test_init(self):
        dir_tests = Directory('src/utils/tests')
        self.assertEqual(dir_tests.path, 'src/utils/tests')
        self.assertEqual(dir_tests.name, 'tests')
        self.assertEqual(
            dir_tests.children[0], File('src/utils/tests/banner.png')
        )
        self.assertTrue(dir_tests == Directory('src/utils/tests'))
