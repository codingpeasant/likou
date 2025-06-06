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
                for k in range(i, j + 1)  # try popping k the last
            )

        return dp(1, len(nums) - 2)

    # TLE
    def maxCoins1(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(nums):
            if len(nums) == 2:
                return 0

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]  # pop i first
                coins += dfs(nums[:i] + nums[i + 1 :])
                maxCoins = max(maxCoins, coins)
            return maxCoins

        return dfs(nums)


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))  # 167
print(s.maxCoins([2, 3, 4]))
