from unittest import TestCase
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        max_num = nums[0]
        for i in range(1, len(nums)):
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().maxSubArray([-2]), -2)
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
