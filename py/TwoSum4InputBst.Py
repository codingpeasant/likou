# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import tarfile
from typing import Optional
from tree_node import *


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complement_set = set()

        def dfs(root: TreeNode) -> bool:
            if not root:
                return False
            if root.val in complement_set:
                return True
            complement_set.add(k - root.val)

            return dfs(root.left) or dfs(root.right)

        return dfs(root)


s = Solution()
input = getSampleBST()
print(s.findTarget(input, 7))
