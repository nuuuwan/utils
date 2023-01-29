import time
from unittest import TestCase

from utils import FiledVariable


class TestFiledVariable(TestCase):
    def test_init(self):
        MAX_N = 1_000_000
        VALUE = (MAX_N) * (MAX_N - 1) // 2

        def func_get():
            s = 0
            for i in range(MAX_N):
                s += i
            return s

        fvar = FiledVariable('test_key', func_get)
        fvar.clear()
        self.assertEqual(fvar.key, 'test_key')
        self.assertEqual(fvar.value, VALUE)

        t0 = time.time()
        self.assertEqual(fvar.value, VALUE)
        dt = time.time() - t0
        self.assertLess(dt, 0.001)
