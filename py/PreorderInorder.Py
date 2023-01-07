# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional
from tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : root_index + 1], inorder[:root_index])
        root.right = self.buildTree(
            preorder[root_index + 1 :], inorder[root_index + 1 :]
        )

        return root


s = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

res = s.buildTree(preorder, inorder)


def pre_order_traversal(root):
    print(root.val)
    if root.left:
        pre_order_traversal(root.left)
    if root.right:
        pre_order_traversal(root.right)


pre_order_traversal(res)
