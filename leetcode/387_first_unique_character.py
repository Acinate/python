import collections
import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Build a hashmap that contains the count of every char in string s
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


class TestSolution(unittest.TestCase):
    def test_first_unique_character(self):
        self.assertEqual(Solution().firstUniqChar("leetcode"), 0)
        self.assertEqual(Solution().firstUniqChar("loveleetcode"), 2)
