# https://leetcode.com/problems/minimum-path-sum/

from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1

        @lru_cache(None)
        def dfs(x, y) -> int:
            if x == 0:
                return sum(grid[0][j] for j in range(y + 1))
            if y == 0:
                return sum(grid[i][0] for i in range(x + 1))

            return grid[x][y] + min(dfs(x - 1, y), dfs(x, y - 1))

        return dfs(m, n)


s = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(s.minPathSum(grid))
