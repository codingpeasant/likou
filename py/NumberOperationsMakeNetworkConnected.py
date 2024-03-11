# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/?orderBy=most_votes

from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - len(connections) > 1:
            return -1
        graph = defaultdict(list)
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        seen = [0] * n
        self.numOfNetworks = 0

        def dfs(node: int):
            if seen[node]:
                return
            seen[node] = 1
            for adj in graph[node]:
                dfs(adj)

        for node in range(n):
            if not seen[node]:
                self.numOfNetworks += 1
                dfs(node)
        return self.numOfNetworks - 1


s = Solution()
n = 5
connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
print(s.makeConnected(n, connections))
