# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]

        graph, res = defaultdict(list), [float("inf")] * n
        res[0] = 0
        for redEdge in redEdges:
            graph[redEdge[0]].append((redEdge[1], 1))
        for blueEdge in blueEdges:
            graph[blueEdge[0]].append((blueEdge[1], 2))

        q, level, visited = deque(), 1, set()
        q.append((0, 0))
        visited.add((0, 0))
        while q:
            size = len(q)
            for _ in range(size):
                node, preColor = q.popleft()
                for nextNode, color in graph[node]:
                    if not (nextNode, color) in visited and color != preColor:
                        res[nextNode] = min(res[nextNode], level)
                        q.append((nextNode, color))
                        visited.add(
                            (nextNode, color)
                        )  # only add the node with color because another color might go to the same node
            level += 1
        return [re if re != float("inf") else -1 for re in res]


s = Solution()
n = 3
redEdges = [[0, 1], [0, 2]]
blueEdges = [[1, 0]]
print(s.shortestAlternatingPaths(n, redEdges, blueEdges))
