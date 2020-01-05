import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


class TestSolution(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
