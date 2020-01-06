import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeUtil:
    @staticmethod
    def list_to_linked_list(self, lst: List) -> ListNode:
        head: ListNode = ListNode(lst[0])
        curr: ListNode = head
        for itm in lst[1:]:
            curr.next = ListNode(itm)
            curr = curr.next
        return head

    @staticmethod
    def linked_list_to_list(self, head: ListNode) -> List:
        lst: List = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst


class TestMethods(unittest.TestCase):
    def test_list_to_linked_list(self):
        head: ListNode = ListNodeUtil().list_to_linked_list(self, [1, 2, 3])
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)

    def test_linked_list_to_list(self):
        head: ListNode = ListNodeUtil().list_to_linked_list(self, [1, 2, 3])
        lst: List = ListNodeUtil().linked_list_to_list(self, head)
        self.assertEqual(lst, [1, 2, 3])
