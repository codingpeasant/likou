# https://leetcode.com/problems/possible-bipartition/description/
# DFS,Graph
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

        def dfs(node: int, color: int) -> bool:
            if colors[node] != 0:  # node has been visited
                return color == colors[node]  # current node color has to be expected
            colors[node] = color
            for nextNode in graph[node]:
                if not dfs(nextNode, -color):  # expect the next node to be another
                    return False
            return True

        for node in graph.keys():
            if colors[node] == 0 and not dfs(node, 1):  # first node is colored as 1
                return False
        return True


s = Solution()
n = 5
dislikes = [[1, 2], [1, 3], [2, 4]]
print(s.possibleBipartition(n, dislikes))
