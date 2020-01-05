import unittest


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in s:
            result *= 26
            result += (ord(c) - 65) + 1
        return result


class TestSolution(unittest.TestCase):
    def test_title_to_number(self):
        self.assertEqual(Solution().titleToNumber("A"), 1)  # 26 * 0 + 1
        self.assertEqual(Solution().titleToNumber("AB"), 28)  # 26 * 1 + 2
        self.assertEqual(Solution().titleToNumber("ZY"), 701)  # 26 * 26 + 25
