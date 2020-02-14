from typing import List
from unittest import TestCase


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


class TestSolution(TestCase):
    def test1(self):
        lst1: List = [-1, -100, 3, 99]
        Solution().rotate(lst1, 2)
        self.assertEqual([3, 99, -1, -100], lst1)

    def test2(self):
        lst2: List = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(lst2, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], lst2)
