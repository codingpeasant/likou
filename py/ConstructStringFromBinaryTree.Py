# https://leetcode.com/problems/construct-string-from-binary-tree/

from typing import Optional
from tree_node import *


class Solution:
    res = ""

    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return self.res

        def dfs(node: TreeNode):
            if not node:
                return
            if node is root:
                self.res += str(root.val)
            else:
                self.res += "(" + str(node.val)

            if not node.left and node.right:
                self.res += "()"
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)

            self.res += ")" if not node is root else ""

        dfs(root)
        return self.res


s = Solution()
root = getSampleTree()
print(s.tree2str(root))
