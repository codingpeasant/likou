# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

from collections import defaultdict
from typing import List, Optional
from tree_node import *


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        valueToIndex, self.postIndex = defaultdict(int), len(postorder) - 1
        for index, value in enumerate(inorder):
            valueToIndex[value] = index

        def dfs(left: int, right: int):
            if left > right:
                return None
            rootValue = postorder[self.postIndex]
            self.postIndex -= 1
            cut = valueToIndex[rootValue]
            rootNode = TreeNode(rootValue)
            rootNode.right = dfs(
                cut + 1, right
            )  # must do right first because postorder iterate right then left when postIndex move from len - 1 to 0
            rootNode.left = dfs(left, cut - 1)

            return rootNode

        return dfs(0, self.postIndex)


s = Solution()
inorder = [9, 3, 20]
postorder = [9, 20, 3]
preOrder(s.buildTree(inorder, postorder))
