# https://leetcode.com/problems/minimum-height-trees/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from collections import defaultdict, deque
from typing import List


# topology sorting - go from the leave nodes, remove level by level until there are only 1 or 2 nodes left
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])
        remainingNodes = n
        while remainingNodes > 2: # why 2? because if there are only 1 or 2 nodes left, they are the roots of the min height trees
            leaveCount = len(leaves)
            remainingNodes -= leaveCount
            for _ in range(leaveCount):  # level by level BFS
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:  # became a leaf
                        leaves.append(nei)

        return list(leaves)


s = Solution()
print(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
