# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Blind
# Grind
# Neet

from tree_node import *


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


s = Solution()
root = getSampleBST()
print(s.lowestCommonAncestor(root, TreeNode(1), TreeNode(3)).val)
