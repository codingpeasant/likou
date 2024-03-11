# https://leetcode.com/problems/all-paths-from-source-to-target/description/

from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphMap, target, res = defaultdict(list), len(graph) - 1, []
        for i, el in enumerate(graph):
            graphMap[i] += el

        def dfs(node: int, path: List):
            path.append(node)
            if node == target:
                res.append(path.copy())
                return

            for next in graphMap[node]:
                dfs(next, path)
                path.pop() # backtrace

        dfs(0, [])
        return res


s = Solution()
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(s.allPathsSourceTarget(graph))
