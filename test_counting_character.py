import unittest
from python.counting_character import count

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, count("josdem", 'm'))
        self.assertEqual(3, count("Alabama", 'a'))


if __name__ == '__main__':
    unittest.main()