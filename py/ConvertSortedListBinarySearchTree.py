# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from typing import Optional
from list_node import *
from tree_node import *


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def dfs(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(arr) - 1)


s = Solution()
input = getSampleLinkedList()
output = s.sortedListToBST(input)
preOrder(output)
