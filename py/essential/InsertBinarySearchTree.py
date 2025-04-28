# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# Neet

from typing import Optional
from tree_node import *


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        if root.val >= val:
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root


s = Solution()
input = getSampleBST()
preOrder(s.insertIntoBST(input, 7))
