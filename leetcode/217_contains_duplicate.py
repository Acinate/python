import unittest
from typing import List, Dict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict: Dict = {}
        for n in nums:
            if num_dict.get(n) is None:
                num_dict[n] = True
            else:
                return True
        return False


class TestSolution(unittest.TestCase):
    def test_contains_duplicate(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 2, 4, 5]
        self.assertFalse(Solution().containsDuplicate(list1))
        self.assertTrue(Solution().containsDuplicate(list2))
