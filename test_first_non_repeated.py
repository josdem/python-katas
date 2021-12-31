import unittest
from python.first_non_repeated import *

'''
Given a numbers collection find fist non-repeated number in that collection
When we have: [25, 25, 18, 18, 18, 36, 1, 2, 2, 34] first non-repeated number is 36
'''

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find([25, 25, 18, 18, 18, 36, 1, 2, 2, 34]), 36)

if __name__ == '__main__':
    unittest.main()