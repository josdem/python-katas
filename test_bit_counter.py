import unittest
from python.bit_counter import *

'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(4), 1)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(9), 2)
        self.assertEqual(count_bits(10), 2)

if __name__ == '__main__':
    unittest.main()