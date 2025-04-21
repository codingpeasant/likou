# https://leetcode.com/problems/path-sum-iii/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional
from tree_node import *


class Solution:
    cnt = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, start, s):
            if not root:
                return
            s -= root.val
            if s == 0:
                self.cnt += 1
            dfs(root.left, False, s)
            dfs(root.right, False, s)
            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)

        dfs(root, True, targetSum)
        return self.cnt

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:

        # prefix sums encountered in current path
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # Can remove sums[currSum-targetSum] prefixSums to get target
                count = sums[total - targetSum]

                # Add value of this prefixSum
                sums[total] += 1
                # Explore children
                count += dfs(root.left, total) + dfs(root.right, total)
                # Remove value of this prefixSum (path's been explored)
                sums[total] -= 1

            return count

        return dfs(root, 0)


s = Solution()
print(s.pathSum(getSampleTree(), 8))
