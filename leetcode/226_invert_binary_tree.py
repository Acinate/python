from unittest import TestCase

from datastructures.tree import to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        right: TreeNode = self.invertTree(root.right)
        left: TreeNode = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root


class TestSolution(TestCase):
    def test(self):
        tree: TreeNode = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        tree2: TreeNode = TreeNode(4)
        tree2.left = TreeNode(7)
        tree2.right = TreeNode(2)
        tree2.left.left = TreeNode(9)
        tree2.left.right = TreeNode(6)
        tree2.right.left = TreeNode(3)
        tree2.right.right = TreeNode(1)
        self.assertEqual(to_list(Solution().invertTree(tree)), to_list(tree2))
