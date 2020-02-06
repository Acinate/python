from unittest import TestCase


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(Solution().hammingWeight(0o0000000000000000000000000001011), 3)
        self.assertEqual(Solution().hammingWeight(0o0000000000000000000000010000000), 1)
        self.assertEqual(Solution().hammingWeight(0o11111111111111111111111111111101), 31)
