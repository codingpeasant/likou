# https://leetcode.ca/2016-09-10-285-Inorder-Successor-in-BST/
# Grind

from typing import Optional
from tree_node import *


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = None
        while root:
            if root.val > p.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans
    
s = Solution()
res = s.inorderSuccessor(getSampleBST(), TreeNode(4))
print(res.val if res else None)