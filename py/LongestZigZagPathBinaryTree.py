# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

from typing import Optional
from tree_node import *


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, isLeft, step):
            if not root:
                return
            self.res = max(self.res, step)

            if isLeft:  # to go left
                dfs(root.left, False, step + 1)
                dfs(root.right, True, 1)
            else:
                dfs(root.right, True, step + 1)
                dfs(
                    root.left, False, 1
                )  # if you have to move left even though you should move right, move to left as step 1

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.res


s = Solution()
input = getSampleTree()
print(s.longestZigZag(input))
