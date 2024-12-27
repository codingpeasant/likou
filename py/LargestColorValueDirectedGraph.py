# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/

from collections import defaultdict
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)

        visited = [-1] * len(colors)
        max_colors = defaultdict(lambda: [0] * 26)

        def explore(node): # this adds color backwards from leaf: 4, 3, 2, 1, 0
            # returns if we found a cycle
            if visited[node] == 0:
                return True
            if visited[node] == 1:
                return False

            visited[node] = 0 # assume visited and has a cycle - if its neighbor encountered node, there is a cycle
            mc = [0] * 26 # max color for current node for all the 26 colors
            for neighbor in graph[node]:
                if explore(neighbor):
                    return True
                mc = [max(mc[i], max_colors[neighbor][i]) for i in range(len(mc))]
            mc[ord(colors[node]) - ord("a")] += 1 # add node's self color
            max_colors[node] = mc

            visited[node] = 1 # already counted the colors from the leaf; if encountered again, simply do nothing
            return False

        for v in range(len(colors)):
            if explore(v):
                return -1

        res = 0
        for v in max_colors.keys():
            res = max(res, max(max_colors[v])) # for each node find the max color and find the max color

        return res


s = Solution()
colors = "abaca"
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
print(s.largestPathValue(colors, edges))
