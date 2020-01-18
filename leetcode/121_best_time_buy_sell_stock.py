from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        if len(prices) > 0:
            current: int = prices[-1]
            for i in range(len(prices), 0, -1):
                if current - prices[i - 1] > profit:
                    profit = current - prices[i - 1]
                if prices[i - 1] > current:
                    current = prices[i - 1]
        return profit


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(Solution().maxProfit([1, 2]), 1)
