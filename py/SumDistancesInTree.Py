# https://leetcode.com/problems/sum-of-distances-in-tree/description/?orderBy=most_votes
# DFS,Graph,Tree,Post Order
# https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130583/c-java-python-pre-order-and-post-order-dfs-o-n/

import collections


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N  # count all nodes in it's subtree (including the root)
        ans = [0] * N

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += (
                        ans[child] + count[child]
                    )  # now only ans[0] is the final right value, which is why dfs2 is needed

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = (
                        ans[node] - count[child] + (N - count[child])
                    )  # ans[node] - count[child]: Get 1 step closer to its subtree nodes; (N - count[child]): Every node other than it's subtree node: become 1 step more far away
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans


s = Solution()
n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
print(s.sumOfDistancesInTree(n, edges))
