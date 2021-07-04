import unittest

def disemvowel(string):
    array = list(string)
    result = filter(lambda ch: ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A'
                    and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U', array)
    return ''.join(map(str, result))

class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

if __name__ == '__main__':
    unittest.main()