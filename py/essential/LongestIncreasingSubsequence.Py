# https://leetcode.com/problems/longest-increasing-subsequence/
# Blind
# Neet
# Grind

from functools import lru_cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == 0:
                return 1
            longest = 1

            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    longest = max(longest, dfs(j) + 1)
            return longest

        return max(dfs(i) for i in range(len(nums)))


s = Solution()
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5]))
print(s.lengthOfLIS1([4, 10, 4, 3, 8, 9]))
# 1,2,3,4,5,3,6,4
