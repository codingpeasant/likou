# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Neet

from typing import List, Optional
from tree_node import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res


s = Solution()
root = getSampleTree()
print(s.preorderTraversal(root))
