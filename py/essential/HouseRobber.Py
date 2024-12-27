# https://leetcode.com/problems/house-robber/
# Blind

from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(nums[i] + dfs(i - 2), dfs(i - 1))

        return dfs(len(nums) - 1)


s = Solution()
nums = [2, 7, 9, 3, 1]
print(s.rob(nums))
