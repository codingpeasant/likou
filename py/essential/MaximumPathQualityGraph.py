# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        G = defaultdict(list)
        for x, y, w in edges:
            G[x].append((y, w))
            G[y].append((x, w))

        def dfs(node, visited, gain, cost):
            if node == 0:
                self.ans = max(self.ans, gain)
            for neib, w in G[node]:
                if w <= cost:
                    dfs(
                        neib,
                        visited.union([neib]),
                        gain + (neib not in visited) * values[neib],
                        cost - w,
                    )

        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans


s = Solution()
print(s.maximalPathQuality([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49))

set1 = set([1, 2, 3])
print(set1.union([4]))
