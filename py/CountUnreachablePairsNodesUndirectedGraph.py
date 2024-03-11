# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from collections import defaultdict
from typing import List

# Time Limit Exceeded
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        if n == len(edges):
            return 0

        graph, subGraphs, visited = defaultdict(list), list(), [False] * n
        for this, that in edges:
            graph[this].append(that)
            graph[that].append(this)

        def dfs(node: int) -> int:
            if visited[node]:
                return 0
            visited[node] = True
            res = 1
            for adj in graph[node]:
                res += dfs(adj)
            return res

        for node in range(n):
            num = dfs(node)
            if num > 0:
                subGraphs.append(num)

        sumUnreachable = 0
        # Time Limit Exceeded
        # for i in range(len(subGraphs)):
        #     for j in range(i + 1, len(subGraphs)):
        #         sumUnreachable += subGraphs[i] * subGraphs[j]
        # if we notice, (4 * 2 + 4 * 1) + (2 * 1), we can combine, equation like this,
        # 4 * 2 + (4 + 2) * 1, using this, we can reduce complexity.
        firstGroupCount = subGraphs[0]
        for i in range(1, len(subGraphs)):
            sumUnreachable += firstGroupCount * subGraphs[i]
            firstGroupCount += subGraphs[i]

        return sumUnreachable


s = Solution()
n = 12
edges = [[2, 6], [11, 3], [5, 4], [9, 6]]
print(s.countPairs(n, edges))
