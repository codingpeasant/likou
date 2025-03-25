# https://leetcode.com/problems/diameter-of-binary-tree/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet
# similar with https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from typing import Optional
from tree_node import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            leftMaxDepth = dfs(node.left)
            rightMaxDepth = dfs(node.right)

            self.res = max(self.res, leftMaxDepth + rightMaxDepth)
            return 1 + max(leftMaxDepth, rightMaxDepth)

        dfs(root)
        return self.res


s = Solution()
print(s.diameterOfBinaryTree(getSampleTree()))
print(s.diameterOfBinaryTree(getCompleteTree()))
print(s.diameterOfBinaryTree(getSampleBST()))
