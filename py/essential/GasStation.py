# https://leetcode.com/problems/gas-station/description/
# Neet
# Grind

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if there is a solution, total_surplus at last should be >= 0 after going from 0 to i
        # since there is only 1 solution, we use start to reset if current i doesn't work (surplus < 0)
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(s.canCompleteCircuit(gas=gas, cost=cost))
