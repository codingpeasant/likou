# https://leetcode.com/problems/number-of-islands/

from sre_constants import GROUPREF_IGNORE
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0

        def merge(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for x, y in ((i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1)):
                merge(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    merge(i, j)
                    res += 1
        return res


s = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(s.numIslands(grid))
