import unittest

'''
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
'''

def sort_odds(array):
    odds = []
    for number in array:
        if number % 2 == 1:
            odds.append(number)
    odds.sort()

    return odds

def sort_array(array):
    result = []
    index = 0
    odds = sort_odds(array)

    for n in array:
        if n % 2 == 1:
            result.append(odds[index])
            index += 1
        else:
            result.append(n)
            
    return result        

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]), [])

if __name__ == '__main__':
    unittest.main()