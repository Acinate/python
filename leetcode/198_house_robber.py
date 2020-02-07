from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp: List = [-1] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[len(nums)]


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)
        self.assertEqual(Solution().rob([2, 7, 9, 3, 1]), 12)
