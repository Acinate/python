from math import floor
from unittest import TestCase


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count: int = 0
        while n > 0:
            n = floor(n / 5)
            count += n
        return count


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(0, Solution().trailingZeroes(3))
        self.assertEqual(1, Solution().trailingZeroes(5))
