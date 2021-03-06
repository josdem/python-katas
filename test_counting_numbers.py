import unittest
from python.counting_numbers import *

'''
Given an integer collection, return an array with three elements:
how many of them are positive, how many negative and how many are zeros.
Given: [-4, 3, -9, 0, 4, 1] then expected output is: [3, 2, 1]
'''

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(counter([-4, 3, -9, 0, 4, 1]), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()