# https://leetcode.com/problems/redundant-connection/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # variable to keep track of graph constructed so far
        graph_so_far = collections.defaultdict(list)

        # dfs function to check if path exists between nodes u and v
        def path_exists(u, v, visited: set):
            # we reached to v from u
            if u == v:
                return True

            # mark u as visited
            visited.add(u)

            # iterate through all the neighbors of u and if they are not visited call dfs on them
            for neighbor in graph_so_far[u]:
                if neighbor not in visited:
                    if path_exists(neighbor, v, visited):
                        return True

            return False

        # iterate through all the pairs of edges
        for u, v in edges:
            # if path exists between u and v return that's the answer
            if path_exists(u, v, set()):
                return [u, v]
            else:
                # if path does not exist we add edges to graph
                # this is to guarantee that the last added edge is picked as the res
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)

        return None


s = Solution()
print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1,4]
print(s.findRedundantConnection([[1, 2], [2, 1]]))
