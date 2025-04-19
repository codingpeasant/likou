# https://leetcode.com/problems/symmetric-tree/description/
# DFS,Pre Order
# Grind

from typing import Optional
from tree_node import *


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(leftSubtree: TreeNode, rightSubtree: TreeNode) -> bool:
            if not leftSubtree and not rightSubtree:
                return True
            if (
                not leftSubtree
                or not rightSubtree
                or leftSubtree.val != rightSubtree.val
            ):
                return False
            return dfs(leftSubtree.left, rightSubtree.right) and dfs(
                leftSubtree.right, rightSubtree.left
            )

        return dfs(root.left, root.right)


s = Solution()
tree = getCompleteTree()
print(s.isSymmetric(tree))
