# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/

from collections import defaultdict
import math
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph, self.res = defaultdict(list), 0
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(u, parent):
            cnt = 1
            for v in graph[u]:
                if v == parent:
                    continue  # not moving back
                cnt += dfs(v, u)
            if u != 0:
                self.res += math.ceil(
                    cnt / seats
                )  # number of litters (or cars) for `cnt` people to travel from node `u` to node `parent`
                # Calculating the number of cars gives the amount of fuel consumed because each car would consume a litre of fuel.
            return cnt

        print(dfs(0, -1))
        return self.res


s = Solution()
roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats = 2
print(s.minimumFuelCost(roads, seats))
