# https://leetcode.com/problems/path-sum/

from typing import Optional
from tree_node import *


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


s = Solution()
input = getSampleTree()
print(s.hasPathSum(input, 8))
