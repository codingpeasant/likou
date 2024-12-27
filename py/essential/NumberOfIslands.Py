# https://leetcode.com/problems/number-of-islands/
# Blind

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0

        def dfs(i: int, j: int):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                for row, col in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                    dfs(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res


s = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(s.numIslands(grid))
