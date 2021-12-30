import unittest
from array_diff import *

'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
'''

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(array_diff([1,2],[1]), [2])
        self.assertEqual(array_diff([1,2,2,2,3],[2]), [1,3])

if __name__ == '__main__':
    unittest.main()