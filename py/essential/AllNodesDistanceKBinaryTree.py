# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=problem-list-v2&envId=rabvlt31
# Grind

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from tree_node import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # DFS function to go through the tree and mark the parent of each node in a dictionary
        def getParent(node, parent):
            if node is None:
                return

            parentMap[node] = parent  # mark parent of each node

            getParent(node.left, node)
            getParent(node.right, node)

        # DFS function that gets the nodes at a distance k from the target
        def getNodes(node, cnt):
            if not node or node in seen or cnt > k:
                return

            seen.add(node)
            if cnt == k:
                res.append(node.val)  # append to result when cnt/distance is k
                return

            getNodes(node.left, cnt + 1)
            getNodes(node.right, cnt + 1)
            getNodes(parentMap[node], cnt + 1)

        parentMap = {}
        seen = set()
        res = []
        getParent(root, None)  # call getParent func for 'root' node
        getNodes(target, 0)  # call getNodes func for 'target' node

        return res


s = Solution()
input = getSampleTree()
print(s.distanceK(input, input.right, 2))
