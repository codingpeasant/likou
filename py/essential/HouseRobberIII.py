# https://leetcode.com/problems/house-robber-iii/description/
# Neet

from typing import Optional
from tree_node import *


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(rootNode: TreeNode) -> list[int]:
            if not rootNode:
                return (0, 0)  # (rob self + grandchildren, rob children)
            left = dfs(rootNode.left)
            right = dfs(rootNode.right)

            return (rootNode.val + left[1] + right[1], max(left) + max(right))

        return max(dfs(root))


s = Solution()
input = getSampleTree()
print(s.rob(input))
