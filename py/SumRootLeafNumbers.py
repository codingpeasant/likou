# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

from typing import Optional
from tree_node import *


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: TreeNode, curSum: int):
            if not root:
                return
            curSum = curSum * 10 + root.val
            if not root.left and not root.right:
                self.res += curSum
                return
            dfs(root.left, curSum)
            dfs(root.right, curSum)

        dfs(root, 0)
        return self.res


s = Solution()
input = getSampleTree()
print(s.sumNumbers(input))
