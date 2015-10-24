__author__ = 'root'
import unittest
from test import mul

class MulTestCase(unittest.TestCase):
    def test_mul(self):
        self.assertTrue(mul(9,-5))

if __name__=='__main__':
    unittest.main()