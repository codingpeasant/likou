# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# DFS,Pre Order,Hash Table

from collections import defaultdict
from typing import List
from tree_node import *


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)

        def dfs(placement, level, root: TreeNode) -> None:
            if not root:
                return
            dic[placement].append((level, root.val))
            dfs(placement - 1, level + 1, root.left)
            dfs(placement + 1, level + 1, root.right)

        dfs(0, 0, root)

        result = []
        for placement in sorted(dic.keys()):  # sort col
            temp = []
            for levelNodePair in sorted(
                dic[placement]
            ):  # sort level first then the val
                temp.append(levelNodePair[1])
            result.append(temp)
        return result


s = Solution()
input = getSampleTree()
print(s.verticalTraversal(input))
