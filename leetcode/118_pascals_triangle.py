from unittest import TestCase
from typing import List

# TODO: Dynamic Programming Implementation


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans: List[int] = []
        for r in range(0, numRows):
            arr: List[int] = []
            for c in range(0, r+1):
                if c == 0 or c == r:
                    arr.append(1)
                else:
                    result: int = ans[r - 1][c - 1] + ans[r - 1][c]
                    arr.append(result)
            ans.append(arr)
        return ans


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().generate(5), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ])
