__author__ = 'root'
import unittest
from test import sqr

class SqrTestCase(unittest.TestCase):
    def test_sqr(self):
        self.assertTrue(sqr(-10))

if __name__=='__main__':
    unittest.main()