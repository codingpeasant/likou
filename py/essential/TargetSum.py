# https://leetcode.com/problems/target-sum/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0
            return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

        return dp(0, 0)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
