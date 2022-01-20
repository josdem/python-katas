import numbers
import unittest

def adder(numbers):
    return numbers

class FixedTest(unittest.TestCase):
    def test(self):
        numbers = [15, 20, 4, 8]
        expectedCollection = [6, 2, 4, 8]
        self.assertEqual(adder(numbers), expectedCollection)

if __name__ == '__main__':
    unittest.main()