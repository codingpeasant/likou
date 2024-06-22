# https://leetcode.com/problems/range-sum-of-bst/
# DFS,Pre Order

from typing import Optional
from tree_node import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            return (
                root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )


s = Solution()
input = getSampleBST()
print(s.rangeSumBST(root=input, low=2, high=6))
