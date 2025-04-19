# https://leetcode.com/problems/burst-balloons/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from functools import lru_cache
from typing import List


class Solution:
    # O(n^3)  # O(n^2) space
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(i, j):
            """dp(i, j) represents the maximum coins after bursting all baboons between i and j."""
            if i > j:
                return 0
            if i == j:
                return nums[i - 1] * nums[i] * nums[i + 1]
            return max(
                dp(i, k - 1) + dp(k + 1, j) + nums[i - 1] * nums[k] * nums[j + 1]
                for k in range(i, j + 1) # try to burst each balloon between i and j
            )

        return dp(1, len(nums) - 2)

s= Solution()
print(s.maxCoins([3, 1, 5, 8])) # 167