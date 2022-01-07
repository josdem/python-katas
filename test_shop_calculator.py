import unittest
from python.shop_calculator import *

'''
Monica wants to buy exactly one keyboard and one USB drive from her favorite electronics store.
The store sells N different brands of keyboards and M different brands of USB drives.
Monica has exactly S dollars to spend, and she wants to spend as much of it as possible (i.e., the total cost of her purchase must be maximal).
Given: Amount of money Monica has to spend in electronics as 10
And: Keyboards prices as [3, 1]
And: Usbs' prices as [5, 2, 8]
When: I call to compute method
Then: I will have 9 as result
'''

class FixedTest(unittest.TestCase):
    def test(self):
        amount = 10
        keyboards = [5, 2, 8]
        usbs = [3, 1]
        self.assertEqual(compute(amount, keyboards, usbs), 9)

if __name__ == '__main__':
    unittest.main()