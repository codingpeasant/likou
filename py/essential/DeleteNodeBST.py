# https://leetcode.com/problems/delete-node-in-a-bst/description/
# Neet

from typing import Optional
from tree_node import *


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            # Target node is smaller than current node, search left subtree
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            # Target node is larger than current node, search right subtree
            root.right = self.deleteNode(root.right, key)

        else:
            # Current node is target node
            if (not root.left) or (not root.right):
                # At least one child is empty
                # Target node is replaced by either non-empty child or None
                root = root.left if root.left else root.right

            else:
                # Both children exist
                # Target node is replaced by smallest element of right subtree
                cur = root.right

                while cur.left:
                    cur = cur.left

                root.val = cur.val  # copy
                root.right = self.deleteNode(
                    root.right, cur.val
                )  # then delete the copied value

        return root


s = Solution()
input = getSampleBST()
preOrder(s.deleteNode(input, 1))
