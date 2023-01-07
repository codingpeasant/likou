# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

from typing import Optional
from tree_node import *


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, current: set) -> int:
            if not root:
                return 0
            if root.val in current:
                current.remove(root.val)
            else:
                current.add(root.val)
            if not root.left and not root.right:
                return 1 if len(current) <= 1 else 0

            return dfs(root.left, current.copy()) + dfs(root.right, current.copy())

        return dfs(root, set())


s = Solution()
input = getSampleTree()
print(s.pseudoPalindromicPaths(input))
