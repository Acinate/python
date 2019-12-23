from typing import List, Mapping


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map: Mapping[int, bool] = {}
        for num in nums:
            if num_map.get(num) is None:
                num_map[num] = False
            elif not num_map[num]:
                num_map[num] = True
        for num in nums:
            if not num_map[num]:
                return num
