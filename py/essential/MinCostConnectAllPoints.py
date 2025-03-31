# https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

import collections
import heapq
from typing import List


# Prim's algorithm implementation
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(points)
        # create graph assuming all points are connected
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i].append(
                        (
                            abs(points[j][0] - points[i][0])
                            + abs(points[j][1] - points[i][1]),
                            j,
                        )
                    )

        heap = [
            (0, 0)
        ]  # pick the first point as starting point and the cost to it is 0
        ans = 0
        visited = set()
        while heap:
            weight, to = heapq.heappop(heap)
            if to in visited:
                continue
            ans += weight
            visited.add(to)

            for cost, nei in graph[to]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))

        return ans


s = Solution()
print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # 20
print(s.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]))  # 4
print(s.minCostConnectPoints([[0, 0]]))  # 0
