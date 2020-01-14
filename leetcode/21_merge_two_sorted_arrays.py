import unittest

from datastructures.linked_list import ListNodeUtil


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# TODO: Fix self parameter in convert_to_ll (Stack Overflow)
class TestSolution(unittest.TestCase):
    def test_merge_two_lists(self):
        convert_to_ll = ListNodeUtil().list_to_linked_list
        list1: ListNode = convert_to_ll(self, [1, 2, 4])
        list2: ListNode = convert_to_ll(self, [1, 3, 4])
        list3: ListNode = Solution().mergeTwoLists(list1, list2)
        convert_to_lst = ListNodeUtil().linked_list_to_list
        self.assertEqual(convert_to_lst(self, list3), [1, 1, 2, 3, 4, 4])
