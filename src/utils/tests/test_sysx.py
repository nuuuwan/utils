"""Test."""
import unittest
from utils import sysx
from utils.sysx import str_color


class TestSys(unittest.TestCase):
    """Test."""

    def test_log_metric(self):
        """Test."""
        sysx.log_metrics()

    def test_run(self):
        """Test."""
        output = sysx.run('echo "hello"')
        self.assertEqual(output, ['hello'])

    def test_str_color(self):
        """Test."""
        self.assertEqual(str_color('Hello'), '\x1b[0;31mHello\x1b[0m')
