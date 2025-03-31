# https://leetcode.com/problems/binary-tree-right-side-view/
# Grind
# Neet

from collections import deque
from typing import List, Optional

from tree_node import *


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        res = []

        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                cur: TreeNode = queue.popleft()
                if i == 0:
                    res.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)

        return res


s = Solution()
print(s.rightSideView(getSampleTree()))
