# https://leetcode.ca/2016-09-21-296-Best-Meeting-Point/

from collections import deque
from math import inf
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        dist = [[0] * n for _ in range(m)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
                    distance = 0
                    visited = set([(i,j)])
                    while q:
                        distance+=1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for dir in dirs:
                                rn, cn = r+dir[0], c+dir[1]
                                if 0<=rn<m and 0<=cn<n and (rn,cn) not in visited:
                                    dist[rn][cn]+=distance
                                    q.append((rn, cn))
                                    visited.add((rn,cn))
        res = inf
        for i in range(m):
            for j in range(n):
                res = min(res, dist[i][j])
        return res

s=Solution()
print(s.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print(s.minTotalDistance([[1,1]]))