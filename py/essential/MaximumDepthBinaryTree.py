# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Blind
# Grind
# Neet

from typing import Optional
from tree_node import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: TreeNode, depth: int):
            if not root:
                return
            self.res = max(self.res, depth)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.res


s = Solution()
input = getSampleTree()
print(s.maxDepth(input))
print(s.maxDepth2(input))
