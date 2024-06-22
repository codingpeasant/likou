# https://leetcode.com/problems/unique-paths-iii/
# DFS,Back Tracking

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.empty, self.res = (
            0,
            0,
        )  # empty is to make sure all available squares are visited
        startX, startY, m, n = 0, 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.empty += 1
                if grid[i][j] == 1:
                    startX = i
                    startY = j

        def dfs(x: int, y: int, visited: List[List[bool]]) -> None:
            if not 0 <= x < m or not 0 <= y < n or visited[x][y] or grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                self.res += 1 if self.empty == 0 else 0
                return

            visited[x][
                y
            ] = True  # visited is to make sure the squares are visited only once
            if grid[x][y] == 0:
                self.empty -= 1
            dfs(x, y + 1, visited)
            dfs(x, y - 1, visited)
            dfs(x - 1, y, visited)
            dfs(x + 1, y, visited)
            visited[x][
                y
            ] = False  # free up the square for another possible path to go through
            if grid[x][y] == 0:
                self.empty += 1  # free up the current square

        dfs(startX, startY, [[False for _ in range(n)] for _ in range(m)])
        return self.res


s = Solution()
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
print(s.uniquePathsIII(grid))
