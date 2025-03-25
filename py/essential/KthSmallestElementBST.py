# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind

from math import inf
from typing import Optional

from tree_node import *


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = inf
        self.count = 0

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res


s = Solution()
print(s.kthSmallest(getSampleBST(), 1))
