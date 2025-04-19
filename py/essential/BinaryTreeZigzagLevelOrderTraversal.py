# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Grind

from collections import deque
from typing import Optional, List
from tree_node import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, fromLeftToRight, res = deque(), True, []
        if root:
            q.append(root)

        while q:
            size = len(q)
            levelNodes = []
            for _ in range(size):
                node: TreeNode = q.popleft()
                levelNodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if fromLeftToRight:
                res.append(levelNodes)
            else:
                res.append(levelNodes[::-1])
            fromLeftToRight = not fromLeftToRight
        return res


s = Solution()
tree = getSampleTree()
print(s.zigzagLevelOrder(tree))
