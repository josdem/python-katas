import unittest
import itertools

def find(numbers):
    max = 0
    bigger = numbers[0]
    for n in numbers:
        count = numbers.count(n)
        if (count > max):
            max = count
            bigger = n
    return bigger

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(34, find([31 , 34, 34, 56, 12, 35, 24, 34, 69, 18]))

if __name__ == '__main__':
    unittest.main()