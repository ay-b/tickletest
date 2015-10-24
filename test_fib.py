__author__ = 'root'
import unittest
from test import fib

class FibTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertTrue(fib(5))

if __name__=='__main__':
    unittest.main()