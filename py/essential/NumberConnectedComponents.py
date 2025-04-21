# https://neetcode.io/problems/count-connected-components
# Blind
# Neet
# Grind


from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res, graph = 0, defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = set()

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for node in graph[node]:
                if not node in visited:
                    dfs(node)

        for node in graph.keys():
            if not node in visited:
                res += 1
                dfs(node)

        return res


s = Solution()
print(s.countComponents(6, [[0, 1], [1, 2], [2, 3], [3, 1], [4, 5]]))
