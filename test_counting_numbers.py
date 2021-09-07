import unittest
import unittest

def counter(numbers):
    return numbers

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(counter([-4, 3, -9, 0, 4, 1]), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()