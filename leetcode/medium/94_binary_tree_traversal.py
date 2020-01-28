from typing import List
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res: List[int] = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: List[int]):
        if root is not None:
            if root.left is not None:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right is not None:
                self.helper(root.right, res)


class Test(TestCase):
    def test(self):
        node: TreeNode = TreeNode(1)
        node.left = None
        node.right = TreeNode(2)
        node.right.left = TreeNode(3)
        self.assertEqual(Solution().inorderTraversal(node), [1, 3, 2])
