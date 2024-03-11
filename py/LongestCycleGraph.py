# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        ranks = [float("inf")] * n

        def dfs(node, rank):
            if node in visited or edges[node] == -1:
                return -1

            if ranks[node] < rank:
                return rank - ranks[node]

            ranks[node] = rank
            val = dfs(edges[node], rank + 1)
            visited.add(node)
            return val

        longest_cycle = -1
        for node in range(n):
            cycle_len = dfs(node, 0)
            if cycle_len > 0:
                longest_cycle = max(longest_cycle, cycle_len)

        return longest_cycle


s = Solution()
edges = [3, 3, 4, 2, 3]
print(s.longestCycle(edges))
