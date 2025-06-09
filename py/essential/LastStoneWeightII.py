# https://leetcode.com/problems/last-stone-weight-ii/description/
# Neet

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Divide all numbers into two groups,
        # what is the minimum difference between the sum of two groups.
        # use dp to record the achievable sum of the smaller group.
        total = sum(stones)
        n = len(stones)
        dp = [0] * (total // 2 + 1)

        for i in range(n):
            for halfWeightSub in range(total // 2, stones[i] - 1, -1):
                dp[halfWeightSub] = max(dp[halfWeightSub], dp[halfWeightSub - stones[i]] + stones[i]) # take the current stone or not
            print(dp)

        return total - 2 * dp[total // 2]

s=Solution()
stones = [2, 7, 4, 1, 8, 1]
print(s.lastStoneWeightII(stones))  # Output: 1