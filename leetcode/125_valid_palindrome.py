from unittest import TestCase


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


class TestSolution(TestCase):
    def test(self):
        self.assertTrue(Solution().isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(Solution().isPalindrome("race a car"))
