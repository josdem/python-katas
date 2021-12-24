import unittest
'''
 Counting vowels and consonants. Create two functions one for counting vowels and another for counting consonants
 Given: A string
 When: That string is josdem
 Then: Counting vowels should be 2 and consonants 4
'''

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 'p', 'q', 's', 't', 'v', 'w','x', 'y', 'z']

def countVowels(keyword):
    return len([x for x in keyword if x in vowels])

def countConsonants(keyword):
    return len([x for x in keyword if x in consonants])
   

class FixedTest(unittest.TestCase):
    def test(self):
        keyword = "josdem"
        self.assertEqual(2, countVowels(keyword))
        self.assertEqual(4, countConsonants(keyword))

if __name__ == '__main__':
    unittest.main()