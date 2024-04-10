import unittest
from python.counting_characters import *

'''
 Counting vowels and consonants. Create two functions one for counting vowels and another for counting consonants
 
 Given: A string
 When: That string is josdem
 Then: Counting vowels should be 2 and consonants 4
'''

class FixedTest(unittest.TestCase):
    def test(self):
        keyword = "josdem"
        self.assertEqual(2, countVowels(keyword))
        self.assertEqual(4, countConsonants(keyword))

if __name__ == '__main__':
    unittest.main()