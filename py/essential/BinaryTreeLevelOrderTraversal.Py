# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Blind
# Grind
# Neet

from collections import deque
from typing import Deque, List, Optional

from tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res: List[List[int]] = []
        q: Deque[TreeNode] = deque()
        q.append(root)

        while q:
            qSize = len(q)
            levelNodes = []
            for _ in range(qSize):
                node = q.popleft()
                levelNodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelNodes)
        return res


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

print(s.levelOrder(node1))
