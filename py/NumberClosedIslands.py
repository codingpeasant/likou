# https://leetcode.com/problems/number-of-closed-islands/description/

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
                return
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        m, n = len(grid), len(grid[0])
        for i in range(m):  # mark all edge nodes to exclude the closed island
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        count = 0
        for i in range(1, m - 1):  # now what left is closed island
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count


s = Solution()
grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
print(s.closedIsland(grid))
