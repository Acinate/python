from typing import List
from unittest import TestCase


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


class TestSolution(TestCase):
    def test0(self):
        nums1 = [1, 2, 3, 0, 0, 0]  # m = 3
        nums2 = [2, 5, 6]  # n = 3
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)

    def test1(self):
        nums1 = [0, 0, 0]  # m = 0
        nums2 = [2, 5, 6]  # n = 3
        Solution().merge(nums1, 0, nums2, 3)
        self.assertEqual([2, 5, 6], nums1)

    def test2(self):
        nums1 = [2, 5, 6]  # m = 3
        nums2 = []  # n = 0
        Solution().merge(nums1, 3, nums2, 0)
        self.assertEqual([2, 5, 6], nums1)

    def test3(self):
        nums1 = []  # m = 3
        nums2 = []  # n = 3
        Solution().merge(nums1, 0, nums2, 0)
        self.assertEqual([], nums1)

    def test4(self):
        nums1 = [2, 0]  # m = 1
        nums2 = [1]  # n = 1
        Solution().merge(nums1, 1, nums2, 1)
        self.assertEqual([1, 2], nums1)

    def test5(self):
        nums1 = [4, 5, 6, 0, 0, 0]  # m = 1
        nums2 = [1, 2, 3]  # n = 1
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual([1, 2, 3, 4, 5, 6], nums1)
