# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/?orderBy=most_votes

from collections import defaultdict
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for child, p in enumerate(parent):
            tree[p].append(child)

        # Store the longest path
        # It is updated in dfs
        self.res = 1

        # dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
        def dfs(node):

            # While examine the children,
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node
            # in the sub-tree rooted at this node. max1 >= max2
            max1 = max2 = 0

            for child in tree[node]:
                childMax = dfs(child)
                # This condition makes sure the path is valid.
                if s[child] != s[node]:
                    # Update the length of the top two longest paths.
                    if childMax > max1:
                        max2 = max1
                        max1 = childMax
                    elif childMax > max2:
                        max2 = childMax

            # Update the result.
            # Again, max1+max2+1 means the length of the longest valid path
            # going through this node in the sub-tree rooted at this node.
            self.res = max(self.res, max1 + max2 + 1)

            # Adding 1 for the current node
            return max1 + 1

        dfs(0)
        return self.res


s = Solution()
parent = [-1, 0, 0, 1, 1, 2]
string = "abacbe"
print(s.longestPath(parent, string))
