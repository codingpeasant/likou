# https://leetcode.com/problems/min-cost-climbing-stairs/
# Neet

from functools import lru_cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 2:
            return min(cost)

        dp = [0] * length # dp[i] is the min cost to reach step i
        # dp[0] = cost[0] because we start from step 0
        # dp[1] = cost[1] because we can start from step 1
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)

        @lru_cache(None)
        def dfs(i) -> int:
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            return cost[i] + min(dfs(i - 1), dfs(i - 2))

        return min(
            dfs(n - 1), dfs(n - 2)
        )  # top of the stairs is the position n, which can be from n-1 or n-2


s = Solution()
input = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(input))
print(s.minCostClimbingStairs1(input))
