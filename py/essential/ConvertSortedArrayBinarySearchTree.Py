# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Grind


from typing import List, Optional
from tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # this high-balanced because the there are same number of nodes on both sides of the mid node
        def build(left, right) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)


s = Solution()
nums = [-10, -3, 0, 5, 9]
root = s.sortedArrayToBST(nums)


def preorder(root):
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


preorder(root)
