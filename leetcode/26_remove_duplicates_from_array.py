from typing import List
from unittest import TestCase


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        last = nums[0]
        count = 1
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur > last:
                last = nums[i]
                nums[i] = nums[count]
                nums[count] = last
                count += 1
        nums = nums[0:count]
        return len(nums)


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().removeDuplicates([]), 0)
        self.assertEqual(Solution().removeDuplicates([1]), 1)
        self.assertEqual(Solution().removeDuplicates([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(Solution().removeDuplicates([0, 0, 1, 1, 2, 2]), 3)
        self.assertEqual(Solution().removeDuplicates([0, 1, 2, 3, 4, 5]), 6)
