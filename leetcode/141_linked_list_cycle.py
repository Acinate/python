from typing import List, Dict
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: List) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    def hasCycle2(self, head: ListNode) -> bool:
        lst: Dict = {}
        while head is not None:
            if lst.get(head.val) is None:
                lst[head.val] = True
                head = head.next
            else:
                return True
        return False


class TestSolution(TestCase):
    def test(self):
        node: ListNode = ListNode(3)
        node.next = ListNode(2)
        node.next.next = ListNode(0)
        node.next.next.next = ListNode(-4)
        node.next.next.next = ListNode(2)
        self.assertTrue(Solution().hasCycle(node))
        node: ListNode = ListNode(1)
        self.assertFalse(Solution().hasCycle(node))
        node: ListNode = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(1)
        self.assertTrue(Solution().hasCycle(node))
