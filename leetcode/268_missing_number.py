from typing import List
from unittest import TestCase


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().missingNumber([3, 0, 1]), 2)
        self.assertEqual(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

        self.assertEqual(Solution2().missingNumber([3, 0, 1]), 2)
        self.assertEqual(Solution2().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
