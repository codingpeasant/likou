# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Blind
# Neet
# Grind

from typing import Optional
from tree_node import *


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxValue = float("-inf")

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            leftSum = max(
                0, dfs(root.left)
            )  # only consider this child path if it's positive
            rightSum = max(0, dfs(root.right))

            self.maxValue = max(self.maxValue, leftSum + rightSum + root.val)
            return max(leftSum, rightSum) + root.val  # can only choose one path

        dfs(root)
        return self.maxValue


s = Solution()
input = getSampleTree()
print(s.maxPathSum(input))
