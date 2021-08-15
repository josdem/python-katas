import unittest

'''
Given an integer collection return a sum of its elements
'''

def sum(numbers):
    return len(numbers)  

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sum([5, 4, 1, 2, 9]), 21)
        self.assertEqual(sum([1, 2, 3, 4, 10, 11]), 31)

if __name__ == '__main__':
    unittest.main()
