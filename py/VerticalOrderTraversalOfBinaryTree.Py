# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

from collections import defaultdict
from typing import List
from tree_node import *


class Solution:
    def dfs(self, placement, level, root, dic):
        if not root:
            return
        dic[placement].append((level, root.val))
        self.dfs(placement - 1, level + 1, root.left, dic)
        self.dfs(placement + 1, level + 1, root.right, dic)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.dfs(0, 0, root, dic)
        result = []
        for i in sorted(dic.keys()):  # sort col
            temp = []
            for j in sorted(dic[i]):  # sort level first then the val
                temp.append(j[1])
            result.append(temp)
        return result


s = Solution()
input = getSampleTree()
print(s.verticalTraversal(input))
