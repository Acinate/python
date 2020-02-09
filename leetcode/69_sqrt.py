import math
from unittest import TestCase


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().mySqrt(4), 2)
        self.assertEqual(Solution().mySqrt(8), 2)
