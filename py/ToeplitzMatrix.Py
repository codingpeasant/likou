# https://leetcode.com/problems/toeplitz-matrix/
# Matrix

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            j = 0
            num = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != num:
                    return False
                i = i + 1
                j = j + 1

        for j in range(n):
            i = 0
            num = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != num:
                    return False
                i = i + 1
                j = j + 1

        return True


s = Solution()
matrix = [[1, 2], [2, 2]]
print(s.isToeplitzMatrix(matrix))
