# https://leetcode.com/problems/house-robber/
# Blind
# Neet

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

    def rob1(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


s = Solution()
nums = [2, 7, 9, 3, 1]
print(s.rob(nums))
print(s.rob1(nums))
