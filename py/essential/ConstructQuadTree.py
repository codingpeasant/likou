# https://leetcode.com/problems/construct-quad-tree/description/
# Neet

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(x=0, y=0, n=len(grid)):  # <- (x,y) is the upper-left corner of the quad
            #    and n is the length of the side of the quad

            if all(
                grid[i + x][j + y]
                == grid[x][y]  # <- check whether all elements in the quad are the
                for i in range(n)
                for j in range(n)
            ):  #    same, then the same. If so, then the quad is a leaf ...

                return Node(grid[x][y] == 1, True, None, None, None, None)

            n //= 2

            return Node(
                False,
                False,  # <- ... if not, then divide the quad in four and recuse.
                dfs(x, y, n),
                dfs(x, y + n, n),
                dfs(x + n, y, n),
                dfs(x + n, y + n, n),
            )

        return dfs()


s = Solution()
grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
]
print(s.construct(grid=grid).val)
