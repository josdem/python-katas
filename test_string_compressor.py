import unittest
import itertools

'''
Given a string "aaabbbbcc"
When we call compress method
Then we have a compressed string like "a3b4c2"
'''

def compress(keyword):
    return keyword

class FixedTest(unittest.TestCase):
    def test(self):
        keyword = "aaabbbbcc"
        expectedString = "a3b4c2"
        self.assertEqual(compress(keyword), expectedString)

if __name__ == '__main__':
    unittest.main()