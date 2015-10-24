__author__ = 'root'
import unittest
from test import cube

class CubeTestCase(unittest.TestCase):
    def test_cube(self):
        self.assertTrue(cube(-47))

if __name__=='__main__':
    unittest.main()
