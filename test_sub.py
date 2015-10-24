__author__ = 'root'
import unittest
from test import sub

class SubTestCase(unittest.TestCase):
    def test_sub(self):
        self.assertTrue(sub(-2,-65))

if __name__=='__main__':
    unittest.main()