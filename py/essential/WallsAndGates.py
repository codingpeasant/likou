# https://neetcode.io/problems/islands-and-treasure
# Neet

from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2147483647
        visited = set()

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]==-1 or (i,j) in visited:
                return INF
            if grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            res = INF
            for di, dj in directions:
                ni, nj = i + di, j + dj
                res = min(res, 1+ dfs(ni, nj))
            visited.remove((i,j))
            return res
        
        def dfs2(i: int, j:int, dist: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]==-1 or (i,j) in visited:
                return INF
            if grid[i][j] == 0:
                return dist
            
            visited.add((i,j))
            res = INF
            for di, dj in directions:
                ni, nj = i + di, j + dj
                res = min(res, dfs2(ni, nj, dist+1))
            visited.remove((i,j))
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = dfs2(i, j, 0)

s=Solution()
input=[
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
s.islandsAndTreasure(input)
print(input)