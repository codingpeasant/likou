# https://leetcode.com/problems/minimum-cost-for-tickets/description/

from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayExists, minCostAtDay = [False] * 366, [0] * 366
        for day in days:
            dayExists[day] = True
        for i in range(1, 366):
            if not dayExists[i]:
                minCostAtDay[i] = minCostAtDay[i - 1]  # if this day doesn't exist
            else:
                minCostAtDay[i] = min(
                    minCostAtDay[i - 1] + costs[0],
                    minCostAtDay[max(i - 7, 0)] + costs[1],
                    minCostAtDay[max(i - 30, 0)] + costs[2],
                )  # try to buy 7 day ticket at (i - 7)th day or 30 day ticket at (i - 30)th day
        return minCostAtDay[-1]

    def mincostTickets1(self, days: List[int], costs: List[int]) -> int:
        daysSet = set(days)

        @lru_cache(None)
        def dfs(i) -> int:  # min cost at ith day, starting from day[0]
            if i < days[0]:
                return 0
            if i == days[0]:
                return min(costs)
            if i not in daysSet:
                return dfs(i - 1)
            return min(
                dfs(i - 1) + costs[0],
                dfs(max(0, i - 7)) + costs[1],
                dfs(max(0, i - 30)) + costs[2],
            )

        return dfs(days[-1])


s = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [7, 2, 15]
print(s.mincostTickets(days, costs))
print(s.mincostTickets1(days, costs))
