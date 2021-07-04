import unittest

def maskify(credit_card):
    return credit_card

class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(maskify(""), "")
        self.assertEqual(maskify("123"), "123")
        self.assertEqual(maskify("SF$SDfgsd2eA"), "########d2eA")

if __name__ == '__main__':
    unittest.main()