import unittest
from python.biggest_price import *

'''
Messages with random data are coming! But we just care about prices!
Your task is to implement a function which removes all non-numeric data and return just the biggest price in the collection
Given: messages = ["hi", "2.0", "@#$%", "32.0"]
Then: result = 32.0
'''

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(biggest(['hi', '2.0', '@#$%', '32.0']), 32.0)
        self.assertEqual(biggest(['pair', 'car', '-10.0']), -10.0)
        self.assertEqual(biggest(['main', '3.14', 'yaml']), 3.14)
        


if __name__ == '__main__':
    unittest.main()