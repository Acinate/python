import math
import unittest
from typing import List, Dict


class Solution(object):
    def majorityElement(self, nums: List[int]):
        # find the element that appears n/2 times
        majority: int = math.ceil(len(nums) / 2)
        num_count: Dict[int, int] = {}
        for i in range(len(nums)):
            n = nums[i]
            if num_count.get(n) is None:
                num_count[n] = 1
            else:
                num_count[n] = num_count.get(n) + 1
            if num_count.get(n) >= majority:
                return n
        raise ValueError('Function returned an invalid result!')


class TestSolution(unittest.TestCase):
    def test_majority_element(self):
        arr1 = [3, 2, 3]
        arr2 = [8, 8, 7, 7, 7]
        ans1 = Solution().majorityElement(arr1)
        ans2 = Solution().majorityElement(arr2)
        self.assertEqual(ans1, 3)
        self.assertEqual(ans2, 7)
