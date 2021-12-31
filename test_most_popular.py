import unittest
from python.most_popular import *

'''
Given a collection with numbers: [31 , 34, 56, 34, 12, 35, 24, 34, 69, 18]
Write a function that finds most popular number in the array, in this case 34 because it is the number that appears most often.
'''

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find([31 , 34, 56, 34, 12, 35, 24, 34, 69, 18]), 34)

if __name__ == '__main__':
    unittest.main()