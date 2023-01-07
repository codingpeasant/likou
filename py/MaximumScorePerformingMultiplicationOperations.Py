# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dfs(lo, hi, k):
            """Return max score from nums[lo:hi+1]."""
            if k == len(multipliers):
                return 0
            return max(
                nums[lo] * multipliers[k] + dfs(lo + 1, hi, k + 1),
                nums[hi] * multipliers[k] + dfs(lo, hi - 1, k + 1),
            )

        return dfs(0, len(nums) - 1, 0)


s = Solution()
nums = [-5, -3, -3, -2, 7, 1]
multipliers = [-10, -5, 3, 4, 6]
print(s.maximumScore(nums, multipliers))
