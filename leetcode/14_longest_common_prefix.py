from typing import List
from unittest import TestCase


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        for i in range(0, len(strs)):
            if len(strs[0]) <= i:
                return ""
            c: str = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]

        return strs[0]


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
