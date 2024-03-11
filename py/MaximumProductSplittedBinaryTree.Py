# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

from typing import Optional
from tree_node import *


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getSum(node: TreeNode) -> int:
            if not node:
                return 0
            leftSum = getSum(node.left)
            rightSum = getSum(node.right)
            return node.val + leftSum + rightSum

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            sumSoFar = left + right + node.val
            if node != root:
                self.maxProd = max(self.maxProd, (treeSum - (sumSoFar)) * sumSoFar)
            return sumSoFar

        self.maxProd, treeSum = 0, getSum(root)
        dfs(root)
        return self.maxProd % (10**9 + 7)


s = Solution()
input = getSampleTree()
print(s.maxProduct(input))
