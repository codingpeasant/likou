# https://leetcode.com/problems/same-tree/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet

from typing import Optional

from tree_node import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
print(s.isSameTree(getSampleTree(), getCompleteTree()))
