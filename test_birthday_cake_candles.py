import unittest
from python.birthday_cake_candles import *

'''
It is your birthday! And you want to make it special, so you want to keep only biggest candles in the cake
Your task is to create a function that removes all small candles and just keep the biggest ones.
'''

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(counter([]), [])
        self.assertEqual(counter([1]), [1])
        self.assertEqual(counter([3, 2, 1, 3]), [3, 3])

if __name__ == '__main__' : 
    unittest.main()