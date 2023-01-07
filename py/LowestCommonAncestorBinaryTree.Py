# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from turtle import right
from tree_node import TreeNode


class Solution:
    # his is a tree search and backtrack. When find the values, back track to the first node with results from subtrees
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        # return the subtree that has p or q; if both are null, return right, which is null.
        return left if left else right


s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5
node3.right = node4

print(s.lowestCommonAncestor(node1, node2, node3).val)
