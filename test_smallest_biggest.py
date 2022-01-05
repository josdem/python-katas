import unittest
from python.smallest_biggest import *
'''
Find smaller and biggest numbers in a collection
Given: A collection like [7, 5, 2, 4, 3, 9]
When: I call find method
Then: I will get a collection with [2, 9] values
'''

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find([7, 5, 2, 4, 3, 9]), [2, 9])

if __name__ == '__main__':
    unittest.main()