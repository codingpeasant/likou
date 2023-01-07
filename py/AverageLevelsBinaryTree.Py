# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from collections import deque
from tree_node import *
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_avg = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_avg.append(sum(level) / len(level))
        return level_avg


s = Solution()
root = getSampleTree()
print(s.averageOfLevels(root))
