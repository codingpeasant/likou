# https://leetcode.ca/2016-10-12-317-Shortest-Distance-from-All-Buildings/

from cmath import inf
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        total = 0 # total building count
        # cnt: how many buildings can reach (x,y)
        #      if there is a column all blockers, then (x,y) cannot reach every building
        cnt = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    q.append((i, j))
                    distance = 0
                    vis = set() # reset for every free-land
                    while q:
                        distance += 1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for xn, yn in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                x, y = r + xn, c + yn
                                if (
                                    0 <= x < m
                                    and 0 <= y < n
                                    and grid[x][y] == 0
                                    and (x, y) not in vis
                                ):
                                    cnt[x][y] += 1
                                    dist[x][y] += distance
                                    q.append((x, y))
                                    vis.add((x, y))
        ans = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == total:
                    ans = min(ans, dist[i][j])
        return -1 if ans == inf else ans

s=Solution()
print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))