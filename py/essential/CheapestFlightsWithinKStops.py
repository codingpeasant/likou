# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Neet
# Grind

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph, visited, self.res = defaultdict(list), set(), float("inf")
        for start,end,cost in flights:
            graph[start].append((end, cost))

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
    
    # dijkstra
    def findCheapestPrice1(self, n, flights, src, dst, k):
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

s = Solution()
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
print(s.findCheapestPrice(n, flights, 0, 3, 1))
print(s.findCheapestPrice1(n, flights, 0, 3, 1))
