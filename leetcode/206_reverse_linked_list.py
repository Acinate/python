import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head


class TestSolution(unittest.TestCase):
    def test_reverse_list(self):
        linked_list = ListNode(1)
        linked_list.next = ListNode(2)
        linked_list.next.next = ListNode(3)
        rev_linked_list = ListNode(3)
        rev_linked_list.next = ListNode(2)
        rev_linked_list.next.next = ListNode(1)
        linked_list = Solution().reverseList(linked_list)
        self.assertEqual(linked_list.val, rev_linked_list.val)
