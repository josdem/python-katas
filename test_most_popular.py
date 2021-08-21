import unittest
import itertools

def find(numbers):
    max = 0
    bigger = numbers[0]
    for k, v in itertools.groupby(numbers, lambda n: numbers.count(n)):
        if(k > max):
            max = k
            bigger = list(v)[0]
    return bigger

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(34, find([31 , 34, 56, 34, 12, 35, 24, 34, 69, 18]))

if __name__ == '__main__':
    unittest.main()