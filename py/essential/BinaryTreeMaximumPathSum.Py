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

    def maxPathSumFromLeafToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(curNode: TreeNode):
            if not curNode:
                return 0

            if not curNode.left and not curNode.right:
                return curNode.val

            leftSum = dfs(curNode.left)
            rightSum = dfs(curNode.right)

            if curNode.left and curNode.right:
                self.res = max(self.res, curNode.val + leftSum + rightSum)
            return max(leftSum, rightSum) + curNode.val

        dfs(root)
        return self.res


s = Solution()
input = getSampleTree()
print(s.maxPathSum(input))
print(s.maxPathSumFromLeafToLeaf(input))
