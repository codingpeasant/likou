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
            self.maxProd = max(
                self.maxProd, left * (treeSum - left), right * (treeSum - right)
            )
            return left + right + node.val

        # when you need to update a variable in a function, you need self.variable, readonly doesn't need self
        self.maxProd, treeSum = 0, getSum(root)
        dfs(root)
        return self.maxProd % (10**9 + 7)


s = Solution()
input = getSampleTree()
print(s.maxProduct(input))
