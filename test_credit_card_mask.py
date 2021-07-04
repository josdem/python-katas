import re
import unittest

def maskify(credit_card):
    SUFFIX_LENGTH = 4
    if len(credit_card) <= SUFFIX_LENGTH:
      return credit_card
    else:
      return re.sub(".", "#", credit_card[0:len(credit_card) - SUFFIX_LENGTH]) + credit_card[len(credit_card) - SUFFIX_LENGTH: len(credit_card)]
      
class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(maskify(""), "")
        self.assertEqual(maskify("123"), "123")
        self.assertEqual(maskify("SF$SDfgsd2eA"), "########d2eA")

if __name__ == '__main__':
    unittest.main()