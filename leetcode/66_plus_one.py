from typing import List
from unittest import TestCase


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[i] += 1
                break
        return digits


class Test(TestCase):
    def test(self):
        self.assertEqual(Solution().plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(Solution().plusOne([0]), [1])
        self.assertEqual(Solution().plusOne([9]), [1, 0])
        self.assertEqual(Solution().plusOne([9, 9, 9]), [1, 0, 0, 0])
