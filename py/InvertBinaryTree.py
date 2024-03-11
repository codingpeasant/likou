# https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional
from tree_node import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        leftTree = root.left
        rightTree = root.right
        root.left = self.invertTree(rightTree)
        root.right = self.invertTree(leftTree)
        return root


s = Solution()
input = getSampleTree()
output = s.invertTree(input)
preOrder(output)
