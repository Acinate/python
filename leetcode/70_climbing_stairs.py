from unittest import TestCase
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp: List[any] = [None] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().climbStairs(2), 2)
        self.assertEqual(Solution().climbStairs(3), 3)
