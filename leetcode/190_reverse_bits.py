from unittest import TestCase


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans


class TestSolution(TestCase):
    def test(self):
        self.assertEqual(0o0111001011110000010100101000000, Solution().reverseBits(0o0000010100101000001111010011100))
