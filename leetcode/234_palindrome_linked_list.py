from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node: ListNode = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


class TestSolution(TestCase):
    def test(self):
        node1: ListNode = ListNode(1)
        node1.next = ListNode(2)
        self.assertFalse(Solution().isPalindrome(node1))
        node2: ListNode = ListNode(1)
        node2.next = ListNode(2)
        node2.next.next = ListNode(2)
        node2.next.next.next = ListNode(1)
        self.assertTrue(Solution().isPalindrome(node2))
