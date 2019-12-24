from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start: int = 0
        end: int = len(s) - 1
        while start < end:
            swap = s[start]
            s[start] = s[end]
            s[end] = swap
            start += 1
            end -= 1
