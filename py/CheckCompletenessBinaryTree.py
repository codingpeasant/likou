# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

from collections import deque
from typing import Optional
from tree_node import *


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q, gotNone = deque(), False
        q.append(root)

        while q:
            node: TreeNode = q.popleft()
            # when true, stop adding more nodes and start to examine if there is any none-null nodes after
            if not node:
                gotNone = True
            elif node and gotNone:
                return False
            elif node:
                q.append(node.left)
                q.append(node.right)

        return True


s = Solution()
input = getCompleteTree()
print(s.isCompleteTree(input))
