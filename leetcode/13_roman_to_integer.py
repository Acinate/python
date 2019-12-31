import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        v = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                v -= roman[s[i]]
            else:
                v += roman[s[i]]
        return v + roman[s[-1]]


class TestSolution(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(3, Solution().romanToInt("III"))
        self.assertEqual(4, Solution().romanToInt("IV"))
        self.assertEqual(9, Solution().romanToInt("IX"))
        self.assertEqual(58, Solution().romanToInt("LVIII"))
        self.assertEqual(1994, Solution().romanToInt("MCMXCIV"))
