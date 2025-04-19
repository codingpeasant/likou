# https://leetcode.com/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet
# Grind

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        zeroRows, zeroCol = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows[i] = True
                    zeroCol[j] = True

        for i in range(m):
            for j in range(n):
                if zeroRows[i] or zeroCol[j]:
                    matrix[i][j] = 0


s = Solution()
inputMatrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s.setZeroes(inputMatrix)
print(inputMatrix)
