from unittest import TestCase
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        prime: List[bool] = [True] * n
        count: int = 0
        prime[0] = False
        prime[1] = False

        for i in range(2, n):
            if prime[i]:
                count += 1
                j: int = 2
                while (j * i) < n:
                    prime[j * i] = False
                    j += 1

        return count


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(4, Solution().countPrimes(10))
