# https://leetcode.com/problems/subtree-of-another-tree/?envType=problem-list-v2&envId=oizxjoit
# Blind

from typing import Optional

from tree_node import *


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q  # either is null or both


s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(1)
node1.left = node2
print(s.isSubtree(node1, TreeNode(1)))
