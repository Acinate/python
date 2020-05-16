from typing import List
from unittest import TestCase


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


class TestSolution(TestCase):
    def test1(self):
        input: List[str] = ["flower", "flow", "flight"]
        self.assertEqual(Solution().longestCommonPrefix(input), "fl")

    def test2(self):
        input: List[str] = ["dog", "racecar", "car"]
        self.assertEqual(Solution().longestCommonPrefix(input), "")

    def test3(self):
        input: List[str] = [""]
        self.assertEqual(Solution().longestCommonPrefix(input), "")

    def test4(self):
        input: List[str] = ["c", "c"]
        self.assertEqual(Solution().longestCommonPrefix(input), "c")
