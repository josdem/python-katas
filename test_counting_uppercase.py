import unittest

from python.counting_uppercase import count

'''
Given A string
When we call count uppercase method
Then I count how many characters are uppercase
And I validate it does not contain spaces
'''

class TestCountingUppercase(unittest.TestCase):
    def test(self):
        self.assertEqual(count("abc"), 0)
        self.assertEqual(count("abcABC123"), 3)
        self.assertEqual(count("abcABC123!@€"), 3)

if __name__ == '__main__':
    unittest.main()        