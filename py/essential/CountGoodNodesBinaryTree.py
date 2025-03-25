# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from tree_node import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.res += 1
            dfs(node.left, max(node.val, max_val))
            dfs(node.right, max(node.val, max_val))

        dfs(root, root.val)
        return self.res


s = Solution()
print(s.goodNodes(getSampleTree()))
