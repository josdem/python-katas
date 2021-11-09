import unittest

'''
I have two arrays with integers. I want to return elements in common.
Given: [1,2,3,4,5] and [1,3,5,7,9] then expected output: [1,3,5]
'''

def find(first, second):
    return first + second

class FixedTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find([1,2,3,4,5], [1,3,5,7,9]), [1,3,5])

if __name__ == '__main__':
    unittest.main()