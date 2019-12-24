import unittest


class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


class SolutionTest(unittest.TestCase):
    def test_move_zeros(self):
        arr1 = [0, 1, 0, 3, 12]
        arr2 = [1, 3, 12, 0, 0]
        Solution().moveZeroes(arr1)
        self.assertEqual(arr1, arr2)
