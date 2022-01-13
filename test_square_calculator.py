import unittest
from python.square_calculator import *

class FixedTest(unittest.TestCase):
    def test(self):
        numbers = [1, 2, 3, 7, 9, 12, 15]
        squared = [1, 4, 9, 49, 81, 144, 225]
        self.assertEqual(square(numbers), squared)

if __name__ == '__main__':
    unittest.main()