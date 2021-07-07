import unittest

'''
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string):
    array = list(string)
    result = filter(lambda ch: ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A'
                    and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U', array)
    return ''.join(result)

class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

if __name__ == '__main__':
    unittest.main()