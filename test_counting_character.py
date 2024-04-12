import unittest
from python.counting_character import count

'''
Given: A string
When: We call count character method
Then: I count how many times this character appears in the string
'''

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, count("josdem", 'm'))
        self.assertEqual(3, count("Alabama", 'a'))


if __name__ == '__main__':
    unittest.main()