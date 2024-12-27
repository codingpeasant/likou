# https://leetcode.com/problems/is-graph-bipartite/description/

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True


s = Solution()
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(s.isBipartite(graph))
