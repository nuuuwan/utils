from unittest import TestCase

from utils import Directory, File


class TestDirectory(TestCase):
    def test_init(self):
        dir_tests = Directory('tests')
        self.assertEqual(dir_tests.path, 'tests')
        self.assertEqual(dir_tests.name, 'tests')
        self.assertEqual(dir_tests.children[0], File('tests/banner.png'))
        self.assertTrue(dir_tests == Directory('tests'))
