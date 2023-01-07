# https://leetcode.com/problems/jump-game/description/

from functools import lru_cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # Time Limit Exceeded
        @lru_cache(None)
        def dfs(index: int) -> bool:
            if index >= n - 1:
                return True
            for i in range(1, nums[index] + 1):
                if dfs(index + i):
                    return True
            return False

        maxDistance = 0
        for i in range(n):
            if i > maxDistance:
                return False
            maxDistance = max(maxDistance, i + nums[i])

        return True

        # return dfs(0)


s = Solution()
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))
