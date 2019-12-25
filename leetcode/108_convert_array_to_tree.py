import unittest
from typing import List

from datastructures.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode or None:
        # insert each element into the tree
        if nums is None:
            return None
        else:
            return self.insert_node(nums, 0, len(nums) - 1)

    def insert_node(self, nums: List[int], start: int, end: int):
        if start > end:
            return None
        mid: int = round((start + end) / 2)
        node: TreeNode = TreeNode(nums[mid])
        node.left = self.insert_node(nums, start, mid - 1)
        node.right = self.insert_node(nums, mid + 1, end)
        return node


class TestSolution(unittest.TestCase):
    def test_sorted_array_to_bst(self):
        input = [-10, -3, 0, 5, 9]
        tree: TreeNode or None = Solution().sortedArrayToBST(input)
        self.assertEqual(tree.val, 0)
        self.assertEqual(tree.left.val, -10)
        self.assertEqual(tree.right.val, 9)
        self.assertEqual(tree.left.right.val, -3)
        self.assertEqual(tree.right.left.val, 5)
