# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacency_list = defaultdict(list)

        for src_node, dst_node in edges:
            adjacency_list[src_node].append(dst_node)
            adjacency_list[dst_node].append(src_node)

        visited = set()

        def collect_in_dfs(cur_node):
            visited.add(cur_node)
            cost_of_collect = 0

            for child_node in adjacency_list[cur_node]:
                if child_node in visited:
                    continue

                cost_from_child = collect_in_dfs(child_node)

                if cost_from_child or hasApple[child_node]:
                    # update cost of collection (i.e., cost of green arrows)
                    # The first +1 is for path from cur_node to child_node, and the second +1 is for going back.
                    cost_of_collect += cost_from_child + 2
            return cost_of_collect

        return collect_in_dfs(0)


s = Solution()
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
print(s.minTime(n, edges, hasApple))
