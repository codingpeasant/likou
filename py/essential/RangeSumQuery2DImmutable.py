# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# Neet

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        self.m = len(matrix)
        self.n = len(matrix[0]) if matrix else 0
        self.prefixSum = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.prefixSum[i][j] = (
                    self.prefixSum[i - 1][j]
                    + self.prefixSum[i][j - 1]
                    - self.prefixSum[i - 1][j - 1]
                    + matrix[i - 1][j - 1]
                )
        print(self.prefixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row1][col2 + 1]
            - self.prefixSum[row2 + 1][col1]
            + self.prefixSum[row1][col1]
        )


s = NumMatrix([[3, 0, 1], [5, 6, 3], [7, 8, 9]])
print(s.sumRegion(0, 0, 2, 2))
print(s.sumRegion(1, 1, 2, 2))
