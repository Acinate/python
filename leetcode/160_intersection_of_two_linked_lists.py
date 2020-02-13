from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa


class TestSolution(TestCase):
    def test1(self):
        lstA = ListNode(4)
        lstA.next = ListNode(1)
        lstA.next.next = ListNode(8)
        lstA.next.next.next = ListNode(4)
        lstA.next.next.next.next = ListNode(5)
        lstB = ListNode(5)
        lstB.next = ListNode(0)
        lstB.next.next = ListNode(1)
        lstB.next.next.next = lstA.next.next
        self.assertEqual(lstA.next.next, Solution().getIntersectionNode(lstA, lstB))
