# https://leetcode.com/problems/minimum-path-sum/
# Neet

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
    
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] += dp[i-1][0] + grid[i][0]

        for i in range(1, n):
            dp[0][i] += dp[0][i-1]+ grid[0][i]

        print(dp)
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]

s = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(s.minPathSum1(grid))
