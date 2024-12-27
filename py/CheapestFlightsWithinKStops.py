# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph, visited, self.res = defaultdict(list), set(), float("inf")
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        def dfs(current: int, stop: int, cost: int):
            if stop > k:
                return
            if current == dst:
                self.res = min(self.res, cost)
                return
            for next in graph[current]:
                if next[0] == src or next in visited:
                    continue
                visited.add(next)
                dfs(next[0], stop + 1, cost + next[1])
                visited.remove(next)

        dfs(src, -1, 0)
        return self.res if self.res < float("inf") else -1


s = Solution()
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
print(s.findCheapestPrice(n, flights, 0, 3, 1))
