# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional

from tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []

        queue.append(root)

        while queue:
            length = len(queue)
            temp = []
            for i in range(0, length):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
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

print(s.levelOrder(node1))
