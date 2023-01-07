# https://leetcode.com/problems/unique-paths-iii/

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.empty = 0
        startX, startY, m, n = 0, 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.empty += 1
                if grid[i][j] == 1:
                    startX = i
                    startY = j

        def dfs(x: int, y: int, visited: List[List[bool]]) -> int:
            if not 0 <= x < m or not 0 <= y < n or visited[x][y] or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if self.empty == 0 else 0

            res = 0
            visited[x][y] = True
            if grid[x][y] == 0:
                self.empty -= 1
            res += dfs(x, y + 1, visited)
            res += dfs(x, y - 1, visited)
            res += dfs(x - 1, y, visited)
            res += dfs(x + 1, y, visited)
            visited[x][y] = False
            if grid[x][y] == 0:
                self.empty += 1
            return res

        return dfs(startX, startY, [[False for _ in range(n)] for _ in range(m)])


s = Solution()
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(s.uniquePathsIII(grid))
