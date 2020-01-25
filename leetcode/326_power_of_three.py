from math import pow
from unittest import TestCase


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        exp: int = 0
        while pow(3, exp) < n:
            exp += 1
        return pow(3, exp) == n

    def isPowerOfThree2(self, n: int) -> bool:
        # 3^19 is largest number less than maximum integer
        # 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0


class TestSolution(TestCase):
    def test(self):
        self.assertFalse(Solution().isPowerOfThree(0))
        self.assertTrue(Solution().isPowerOfThree(1))
        self.assertTrue(Solution().isPowerOfThree(9))
        self.assertTrue(Solution().isPowerOfThree(27))
        self.assertFalse(Solution().isPowerOfThree(45))

    def test2(self):
        self.assertFalse(Solution().isPowerOfThree2(0))
        self.assertTrue(Solution().isPowerOfThree2(1))
        self.assertTrue(Solution().isPowerOfThree2(9))
        self.assertTrue(Solution().isPowerOfThree2(27))
        self.assertFalse(Solution().isPowerOfThree2(45))
