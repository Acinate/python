from typing import List, Mapping

test_nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map: Mapping[int, bool] = {}
        for num in nums:
            if num_map[num] is None:
                num_map[num] = False
            elif not num_map[num]:
                num_map[num] = True
        for num in nums:
            if not num_map[num]:
                return num


ans = Solution().singleNumber(test_nums)
print(ans)
