# https://leetcode.com/problems/evaluate-division/submissions/953669369/
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Step 1. Build the Graph
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)

        # Step 2. DFS function
        def dfs(x, y, visited: set):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0

            # x points to y
            if y in graph[x]:
                return graph[x][y]

            # x maybe connected to y through other nodes
            # use dfs to see if there is a path from x to y
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else: # a/b (2) * b/c (3) = a/c (6)
                        return graph[x][i] * temp
            return -1

        # go through each of the queries and find the value
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res


s = Solution()
print(
    s.calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)
