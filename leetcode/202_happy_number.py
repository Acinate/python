from math import pow
from unittest import TestCase


class Solution:
    def isHappy(self, n: int) -> bool:
        return self.checkHappy(n, {})

    def checkHappy(self, n: int, d: dict):
        cur_sum: int = 0
        num_str: str = str(n)
        for c in num_str:
            cur_sum += int(pow(int(c), 2))
        if cur_sum == 0:
            return False
        elif cur_sum == 1:
            return True
        else:
            if d.get(cur_sum) is not None:
                return False
            else:
                d[cur_sum] = True
                return self.checkHappy(cur_sum, d)


class TestSolution(TestCase):
    def test(self):
        self.assertTrue(Solution().isHappy(19))
        self.assertFalse(Solution().isHappy(2))
