# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind
# Neet

from collections import defaultdict
from typing import List, Optional

from tree_node import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderValueToIndex, self.preorderIndex = defaultdict(int), 0
        for index, value in enumerate(inorder):
            inorderValueToIndex[value] = index

        def dfs(leftLimit: int, rightLimit: int) -> Optional[TreeNode]:
            if leftLimit > rightLimit:
                return None
            rootValue = preorder[self.preorderIndex]
            self.preorderIndex += 1
            cut = inorderValueToIndex[rootValue]
            rootNode = TreeNode(rootValue)
            rootNode.left = dfs(leftLimit, cut - 1)
            rootNode.right = dfs(cut + 1, rightLimit)
            return rootNode

        return dfs(0, len(inorder) - 1)


s = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
preOrder(s.buildTree(preorder, inorder))
