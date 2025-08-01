import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "../src")))

from pchjlib import vi_tri_so_Fibonacci, InvalidInputError
import unittest


class TestFibonacci(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(vi_tri_so_Fibonacci(0), 0)
        self.assertEqual(vi_tri_so_Fibonacci(1), 1)
        self.assertEqual(vi_tri_so_Fibonacci(10), 55)

    def test_invalid(self):
        with self.assertRaises(InvalidInputError):
            vi_tri_so_Fibonacci(3.14)


if __name__ == "__main__":
    unittest.main()
