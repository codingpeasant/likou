# https://leetcode.com/problems/rotting-oranges/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res, freshCount = 0, 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                if grid[i][j] == 1:
                    freshCount += 1
        if freshCount == 0:
            return 0
        while rotten:
            for _ in range(len(rotten)):
                curRotten = rotten.pop(0)
                for dir in dirs:
                    newX = curRotten[0] + dir[0]
                    newY = curRotten[1] + dir[1]
                    if (
                        newX < 0
                        or newY < 0
                        or newX > m - 1
                        or newY > n - 1
                        or grid[newX][newY] != 1  # nothing to rot
                    ):
                        continue
                    freshCount -= 1
                    grid[newX][newY] = 2
                    rotten.append([newX, newY])
            res += 1
        return res - 1 if freshCount == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
