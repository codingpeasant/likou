# https://leetcode.ca/2021-03-13-1730-Shortest-Path-to-Get-Food/
# Grind

from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        """
        BFS to find the shortest path to get food.
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        visited = set()

        # Find the starting point
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    visited.add((i, j))
                    break
            if queue:
                break

        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if grid[x][y] == '#':
                    return steps
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != 'X':
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            steps += 1

        return -1
  
s=Solution()
print(s.getFood([["X", "X", "X", "X", "X"], ["X", "*", "O", "O", "X"], ["X", "O", "#", "O", "X"], ["X", "X", "X", "X", "X"]]))
grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
print(s.getFood(grid))