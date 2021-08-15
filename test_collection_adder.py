import unittest

'''
Given an integer collection return a sum of its elements
'''

def adder(numbers):
    return sum(numbers)  

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(adder([5, 4, 1, 2, 9]), 21)
        self.assertEqual(adder([1, 2, 3, 4, 10, 11]), 31)

if __name__ == '__main__':
    unittest.main()
