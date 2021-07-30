import re
from typing import Pattern
import unittest

'''
Messages with random data are coming! But we just care about prices!
Your task is to implement a function which removes all non numeric data and return just the biggest price in the collection
messages = ["hi", "2.0", "@#$%", "32.0"]
result = 32.0
'''

pattern = '-?[0-9]+.?[0-9]+'

def biggest(data):
    return float(max([l for l in data if re.match(pattern, l)]))

class FixedTest(unittest.TestCase):

    def test(self):
        self.assertEqual(biggest(['hi', '2.0', '@#$%', '32.0']), 32.0)
        self.assertEqual(biggest(['pair', 'car', '-10.0']), -10.0)
        self.assertEqual(biggest(['main', '3.14', 'yaml']), 3.14)
        


if __name__ == '__main__':
    unittest.main()