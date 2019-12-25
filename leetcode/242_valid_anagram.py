import unittest
from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1: Dict = {}
        dict2: Dict = {}

        if len(s) != len(t):
            return False

        for c in s:
            if dict1.get(c) is None:
                dict1[c] = 1
            else:
                dict1[c] = dict1.get(c) + 1

        for c in t:
            if dict2.get(c) is None:
                dict2[c] = 1
            else:
                dict2[c] = dict2.get(c) + 1

        for k, v in dict1.items():
            if v != dict2.get(k):
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_is_anagram(self):
        str1 = "Hello world"
        str2 = "olleH dlrow"
        self.assertTrue(Solution().isAnagram(str1, str2))
