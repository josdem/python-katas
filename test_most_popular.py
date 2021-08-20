import unittest

def find(numbers):
    return len(numbers)

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(31, find([31 , 34, 34, 56, 12, 35, 24, 34, 69, 18]))

if __name__ == '__main__':
    unittest.main()