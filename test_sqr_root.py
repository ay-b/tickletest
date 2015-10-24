__author__ = 'root'
import unittest
from test import sqr_r

class SqrRTestCase(unittest.TestCase):
    def test_sqr_r(self):
        self.assertTrue(sqr_r(5))

if __name__=='__main__':
    unittest.main()
