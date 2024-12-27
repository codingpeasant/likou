# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional
from tree_node import *


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, depthLeft: int, depthRight: int) -> int:
            if not root:
                return 0

            if depthLeft == depthRight:
                return (1 << depthLeft) - 1

            return (
                1
                + dfs(root.left, leftDepth(root.left), rightDepth(root.left))
                + dfs(root.right, leftDepth(root.right), rightDepth(root.right))
            )

        def rightDepth(root: TreeNode):
            res = 0
            while root:
                res += 1
                root = root.right

            return res

        def leftDepth(root: TreeNode):
            res = 0
            while root:
                res += 1
                root = root.left

            return res

        return dfs(root, leftDepth(root), rightDepth(root))


s = Solution()
input = getCompleteTree()
print(s.countNodes(input))
