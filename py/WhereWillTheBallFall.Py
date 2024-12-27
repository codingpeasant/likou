# https://leetcode.com/problems/where-will-the-ball-fall/
# Matrix,Simulation

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []

        for j in range(n):
            cur = j
            for i in range(m):
                next = grid[i][cur] + cur  # move back (-1) or forward (1)
                if next < 0 or next >= n or grid[i][cur] != grid[i][next]:
                    cur = -1
                    break
                cur = next  # move to next level
            res.append(cur)
        return res


s = Solution()
grid = [
    [1, 1, 1, -1, -1],
    [1, 1, 1, -1, -1],
    [-1, -1, -1, 1, 1],
    [1, 1, 1, 1, -1],
    [-1, -1, -1, -1, -1],
]
print(s.findBall(grid))
