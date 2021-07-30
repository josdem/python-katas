import unittest

'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
'''

def maskify(credit_card):
    SUFFIX_LENGTH = 4
    if len(credit_card) <= SUFFIX_LENGTH:
      return credit_card
    else:
      return "#" * (len(credit_card) - SUFFIX_LENGTH) + credit_card[-SUFFIX_LENGTH:]
      
class FixedTest(unittest.TestCase):

    def tests(self):
        self.assertEqual(maskify(""), "")
        self.assertEqual(maskify("123"), "123")
        self.assertEqual(maskify("SF$SDfgsd2eA"), "########d2eA")

if __name__ == '__main__':
    unittest.main()