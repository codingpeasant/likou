# https://leetcode.com/problems/leaf-similar-trees/description/

from typing import Optional
from tree_node import *


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, res: list):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            dfs(root.left, res)
            dfs(root.right, res)

        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)

        return res2 == res1
