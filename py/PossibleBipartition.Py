# https://leetcode.com/problems/possible-bipartition/description/

from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True

        graph, colors = defaultdict(list), defaultdict(int)

        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
            colors[dislike[0]] = 0

        def dfs(node: int, color: int) -> bool:
            if colors[node] != 0:
                return color == colors[node]
            colors[node] = color
            for nextNode in graph[node]:
                if not dfs(nextNode, -color):
                    return False
            return True

        for node in graph.keys():
            if colors[node] == 0 and not dfs(node, 1):
                return False
        return True


s = Solution()
n = 5
dislikes = [[1, 2], [3, 4], [4, 5], [3, 5]]
print(s.possibleBipartition(n, dislikes))
