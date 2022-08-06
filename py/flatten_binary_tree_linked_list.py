# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from turtle import right
from typing import Optional
from tree_node import TreeNode


class Solution:
    pre = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.left = None
        root.right = self.pre
        self.pre = root


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

s.flatten(node1)

while node1:
    print(node1.val)
    node1 = node1.right
