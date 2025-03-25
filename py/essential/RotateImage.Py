# https://leetcode.com/problems/rotate-image/
# Array,Matrix
# Blind
# Neet

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)

        # flip horizontally
        for i in range(m):
            for j in range(m // 2):
                matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]
        # then transpose
        for i in range(m):
            for j in range(m - i):
                matrix[i][j], matrix[m - 1 - j][m - 1 - i] = (
                    matrix[m - 1 - j][m - 1 - i],
                    matrix[i][j],
                )


s = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(matrix)
print(matrix)
