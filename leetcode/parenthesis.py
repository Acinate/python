from unittest import TestCase


class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""


class TestSolution(TestCase):
    def test(self):
        self.assertTrue(Solution().isValid("()"))
        self.assertTrue(Solution().isValid("()[]{}"))
        self.assertFalse(Solution().isValid("(]"))
        self.assertFalse(Solution().isValid("([)]"))
        self.assertTrue(Solution().isValid("{[]}"))
