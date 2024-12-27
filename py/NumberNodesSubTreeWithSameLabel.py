# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

from collections import Counter, defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree, visited, res = defaultdict(list), set(), [0] * n
        for edge in sorted(edges):
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def dfs(root: int) -> Counter:
            visited.add(root)

            parentCounts = Counter(labels[root])  # add 1 to current letter on root
            for child in tree[root]:
                if child in visited:
                    continue
                parentCounts += dfs(
                    child
                )  # Counter object could add directly to add the values on same keys
            res[root] = parentCounts[labels[root]]
            return parentCounts

        dfs(0)
        return res


s = Solution()
n = 5
edges = [[0, 1], [0, 2], [1, 3], [0, 4]]
labels = "aabab"
print(s.countSubTrees(n, edges, labels))
