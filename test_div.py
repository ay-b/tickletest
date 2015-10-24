__author__ = 'root'
import unittest
from test import div

class DivTestCase(unittest.TestCase):
    def test_div(self):
        self.assertFalse(div(-1,0))

if __name__=='__main__':
    unittest.main()