# https://leetcode.com/problems/01-matrix/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from math import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = inf
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.pop(0)
            for dir in directions:
                nx = x + dir[0]
                ny = y + dir[1]
                if (
                    0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[x][y] + 1
                ):  # not visited
                    q.append((nx, ny))
                    mat[nx][ny] = mat[x][y] + 1
        return mat


s = Solution()
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(s.updateMatrix(mat))
