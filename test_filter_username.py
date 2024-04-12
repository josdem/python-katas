import unittest
from python.filter_username import *

'''
Given A username
When I call the function filter_username
Then return true if the username is valid or false if it is not
Crtiteria: Username uppercase ratio should be less than 0.5
'''


class FixedTest(unittest.TestCase):

    def test(self):
        self.assertTrue(filter_username('johndoe'))
        self.assertTrue(filter_username('josdem'))
        self.assertFalse(filter_username('NHUQfuLarRMDj'))
        self.assertFalse(filter_username('rJVyFMNsmXhPUvG'))


if __name__ == '__main__':
    unittest.main()