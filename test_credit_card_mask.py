import unittest

def maskify(credit_card):
    return credit_card

class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(maskify(""), "")

if __name__ == '__main__':
    unittest.main()