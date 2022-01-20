import numbers
import unittest
from python.digital_adder import *

'''
Given: A numeric collection
When: I call add method
Then: I will get a collection with every element summing its digits
'''

class FixedTest(unittest.TestCase):
    def test(self):
        numbers = [15, 20, 4, 8]
        expectedCollection = [6, 2, 4, 8]
        self.assertEqual(adder(numbers), expectedCollection)

if __name__ == '__main__':
    unittest.main()