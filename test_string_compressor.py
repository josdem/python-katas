import unittest

def compress(keyword):
    return keyword

class FixedTest(unittest.TestCase):
    def test(self):
        keyword = "aaabbbbcc"
        expectedString = "a3b4c2"
        self.assertEqual(compress(keyword), expectedString)

if __name__ == '__main__':
    unittest.main()