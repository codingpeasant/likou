# https://leetcode.com/problems/find-duplicate-subtrees/description/

from collections import defaultdict
from typing import List, Optional
from tree_node import *


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        serializedTree, res = defaultdict(int), []

        def dfs(root: TreeNode):
            if not root:
                return "*"
            serialized = str(root.val) + "," + dfs(root.left) + "," + dfs(root.right)
            serializedTree[serialized] += 1
            if serializedTree[serialized] == 2:
                res.append(root)
            return serialized

        dfs(root)
        return res


s = Solution()
input = getSampleTree()
print(s.findDuplicateSubtrees(input))
