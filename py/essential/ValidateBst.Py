# https://leetcode.com/problems/validate-binary-search-tree/
# DFS,Pre Order
# Blind
# Grind
# Neet

from math import inf
from typing import Optional
from tree_node import *


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high) -> bool:
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return helper(root.left, low, root.val) and helper(
                root.right, root.val, high
            )

        return helper(root, -inf, inf)


s = Solution()
root = getSampleBST()
print(s.isValidBST(root))
print(s.isValidBST(getSampleTree()))
