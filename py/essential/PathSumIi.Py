# https://leetcode.com/problems/path-sum-ii/
# Grind

from typing import List
from tree_node import *


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None:
                return None
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans


s = Solution()
input = getSampleTree()
print(s.pathSum(input, 8))
