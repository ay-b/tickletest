__author__ = 'root'
import unittest
from test import add

class AddTestCase(unittest.TestCase):
    def test_add(self):
        self.assertTrue(add(-1,5))

if __name__=='__main__':
    unittest.main()