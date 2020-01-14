import collections
from typing import List
from unittest import TestCase


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())


class TestSolution(TestCase):
    def test_intersect(self):
        self.assertEqual(Solution().intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
