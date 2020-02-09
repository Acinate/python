from typing import List
from unittest import TestCase


class MinStack:
    stack: List

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min is None or cur_min > x:
            cur_min = x
        self.stack.append((x, cur_min))

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) > 0 else None


class TestSolution(TestCase):
    def test(self):
        min_stack: MinStack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.getMin(), -2)
