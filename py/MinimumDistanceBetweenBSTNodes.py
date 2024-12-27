# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from typing import Optional
from tree_node import *


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = float("inf")

        def dfs(root: TreeNode, low: int, high: int):
            if not root:
                return
            self.res = min(self.res, root.val - low, high - root.val)
            dfs(root.left, low, root.val)
            dfs(root.right, root.val, high)

        dfs(root, float("-inf"), float("inf"))
        return self.res


s = Solution()
bst = getSampleBST()
print(s.minDiffInBST(bst))
