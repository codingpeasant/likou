# https://leetcode.com/problems/as-far-from-land-as-possible/

from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # multiple start points for BFS. If use grid[i][j] == 0, we have to try every one from scratch
        # this could be - find the water cell that is furthest from a land
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n or len(q) == 0:
            return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x + i, y + j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level - 1


s = Solution()
grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(s.maxDistance(grid))
