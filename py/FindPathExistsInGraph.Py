# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node: int, visited: set) -> bool:
            if node == destination:
                return True
            visited.add(node)

            for nextNode in graph[node]:
                if nextNode not in visited:
                    if dfs(nextNode, visited):
                        return True
            return False  # every node in source group is visited

        return dfs(source, set())


s = Solution()
edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
print(s.validPath(10, edges, 5, 9))
