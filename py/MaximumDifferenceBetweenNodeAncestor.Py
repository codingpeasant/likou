# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

from tree_node import *


class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        def dfs(node, low, high):
            if not node:
                return

            self.max_diff = max(
                self.max_diff, abs(node.val - low), abs(node.val - high)
            )
            low1, high1 = min(low, node.val), max(high, node.val)
            dfs(node.left, low1, high1)
            dfs(node.right, low1, high1)

        self.max_diff = 0
        dfs(root, root.val, root.val)
        return self.max_diff


s = Solution()
tree = getSampleTree()
print(s.maxAncestorDiff(tree))
