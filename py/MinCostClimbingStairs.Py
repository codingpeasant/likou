# https://leetcode.com/problems/min-cost-climbing-stairs/

from cmath import cos
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 2:
            return min(cost)

        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


s = Solution()
input = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(input))
