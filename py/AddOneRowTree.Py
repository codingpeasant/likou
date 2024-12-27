# https://leetcode.com/problems/add-one-row-to-tree/
# BFS,Tree

from collections import deque
from typing import Optional
from tree_node import *


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        q = deque()
        q.append(root)
        # collect all the nodes in parent level
        for _ in range(depth - 2):
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        while q:
            node = q.popleft()
            tmp = node.left
            node.left = TreeNode(val)
            node.left.left = tmp
            tmp = node.right
            node.right = TreeNode(val)
            node.right.right = tmp

        return root


s = Solution()
root = getSampleTree()
root = s.addOneRow(root, 1, 2)
preOrder(root)
