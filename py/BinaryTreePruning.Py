# https://leetcode.com/problems/binary-tree-pruning/

from typing import Optional
from xmlrpc.client import Boolean
from tree_node import *


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root) -> bool:  # if to keep
            if not root:
                return False

            left_keep = dfs(root.left)
            right_keep = dfs(root.right)
            if not left_keep:
                root.left = None
            if not right_keep:
                root.right = None
            return left_keep or right_keep or root.val != 0

        return root if dfs(root) else None


s = Solution()
node1 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(0)
node4 = TreeNode(0)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5
node3.right = node4

res = s.pruneTree(node1)
preOrder(res)
