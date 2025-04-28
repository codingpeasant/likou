# https://leetcode.com/problems/balanced-binary-tree/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from typing import Optional

from tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1

    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(max(left) - max(right)) > 1:
                self.res = False
            return (max(left) + 1, max(right) + 1)

        dfs(root)
        return self.res


s = Solution()
input = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.isBalanced1(input))
input = TreeNode(
    1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)
)
print(s.isBalanced1(input))
input = TreeNode()
print(s.isBalanced1(input))
input = TreeNode(1)
print(s.isBalanced1(input))
