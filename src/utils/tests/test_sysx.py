"""Test."""
import unittest
from utils import sysx


class TestSys(unittest.TestCase):
    """Test."""

    def test_log_metric(self):
        """Test."""
        sysx.log_metrics()


    def test_run(self):
        """Test."""
        output = sysx.run('echo "hello"')
        self.assertEqual(output, ['hello'])
