import math
from typing import List
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# constructs a Binary Tree Node from a List
def from_list(lst: List[int], node=None, height=0):
    height += 1
    if len(lst) <= 0:
        return node
    if node is None and len(lst) > 0:
        node = TreeNode(lst.pop(0))
    count: int = int(math.pow(2, height))
    items: List[int] = lst[0:count]
    left: List[int] = items[:len(items) // 2]
    right: List[int] = items[len(items) // 2:]
    while items:
        lst.pop(0)
        items.pop(0)
    node.left = from_list(lst, node, height)
    node.right = from_list(lst, node, height)
    return node


# converts a Tree into a List (Breadth First Traversal)
def to_list(node: TreeNode):
    queue: List[TreeNode] = [node]
    values: List[any] = []
    while queue:
        node = queue.pop(0)
        if node is not None:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            values.append(None)
    return trim_list(values)


# trims None values from end of a List
def trim_list(lst: List[int]):
    count: int = 0
    for i in range(len(lst) - 1, 1, -1):
        if lst[i] is None:
            count += 1
        else:
            break
    return lst[0:len(lst) - count]


class TestTreeNode(TestCase):
    def test_to_list(self):
        tree1: TreeNode = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        tree1.left.left = TreeNode(4)
        tree1.left.right = TreeNode(5)
        tree1.right.left = TreeNode(6)
        tree1.right.right = TreeNode(7)
        lst1: List[int] = to_list(tree1)
        self.assertEqual(lst1, [1, 2, 3, 4, 5, 6, 7])

        tree2: TreeNode = TreeNode(1)
        tree2.left = TreeNode(2)
        tree2.right = TreeNode(3)
        tree2.left.left = None
        tree2.left.right = TreeNode(4)
        tree2.right.left = None
        tree2.right.right = TreeNode(5)
        lst2: List[int] = to_list(tree2)
        self.assertEqual(lst2, [1, 2, 3, None, 4, None, 5])

    def test_to_tree(self):
        list1 = [1, 2, 3, 4, 5, 6, 7]
        tree1 = from_list(list1)
        self.assertEqual(to_list(tree1), list1)
