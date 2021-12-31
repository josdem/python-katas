import unittest
from python.string_compressor import *

'''
Given a string "aaabbbbcc"
When we call compress method
Then we have a compressed string like "a3b4c2"
'''

class FixedTest(unittest.TestCase):
    def test(self):
        keyword = "aaabbbbcc"
        expectedString = "a3b4c2"
        self.assertEqual(compress(keyword), expectedString)

if __name__ == '__main__':
    unittest.main()