# https://leetcode.com/problems/shortest-bridge/description/
# DFS,BFS,Matrix

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, step, bfs = len(grid), 0, deque()

        def dfs(i, j):
            grid[i][j] = -1  # mark as visited
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        return i, j

        dfs(*first())
        while bfs:
            size = len(bfs)
            for _ in range(size):
                i, j = bfs.popleft()

                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return step
                        elif not grid[x][y]:
                            grid[x][y] = -1  # mark as visited
                            bfs.append((x, y))
            step += 1


s = Solution()
grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
print(s.shortestBridge(grid))
