# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
# Grind

from typing import Optional
from tree_node import *


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # queue for keeping track
        q = [(0, root)]
        ans = 0
        while q:
            n = len(q)
            # nodes list to store indexes of all nodes at a level
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)
                if node.left:
                    q.append((2 * idx + 1, node.left))
                if node.right:
                    q.append((2 * idx + 2, node.right))
            # max of ans or (right-most index - left-most index + 1) for a level
            print(nodes)
            ans = max(ans, max(nodes) - min(nodes) + 1)
        return ans


s = Solution()
input = getSampleTree()
print(s.widthOfBinaryTree(input))
