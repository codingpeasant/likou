# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List, Optional

from tree_node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        res = []

        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(0, size):
                cur = queue.pop(0)
                if i == size - 1:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res


s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5
node3.right = node4

print(s.rightSideView(node1))
