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

    def maxAncestorDiff1(self, root: TreeNode):  # post order
        self.maxDiff = 0

        def dfs(node: TreeNode):
            if not node:
                return float("inf"), -1
            lowLeft, highLeft = dfs(node.left)
            lowRight, highRight = dfs(node.right)
            low = min(lowLeft, lowRight)
            high = max(highLeft, highRight)
            if low != float("inf") and high != -1:
                self.maxDiff = max(
                    self.maxDiff, abs(node.val - low), abs(high - node.val)
                )
            return min(low, node.val), max(high, node.val)

        dfs(root)
        return self.maxDiff


s = Solution()
tree = getSampleTree()
print(s.maxAncestorDiff(tree))
print(s.maxAncestorDiff1(tree))
