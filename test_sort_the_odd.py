import unittest

'''
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
'''

def sort_array(array):
    odds = sorted((n for n in array if n % 2 == 1), reverse=True)
    return [n if n % 2 == 0 else odds.pop() for n in array]

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]), [])

if __name__ == '__main__':
    unittest.main()