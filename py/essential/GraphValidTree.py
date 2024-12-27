from collections import defaultdict
from typing import List

# https://neetcode.io/problems/valid-tree
# Blind


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        visited = set()
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        def dfs(node: int, prevNode: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == prevNode:
                    continue
                if not dfs(node=nei, prevNode=node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


s = Solution()
print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
