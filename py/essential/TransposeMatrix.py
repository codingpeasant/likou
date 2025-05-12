# https://leetcode.com/problems/transpose-matrix/description/
# Neet

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res


s = Solution()
print(s.transpose([[1, 2, 3], [4, 5, 6]]))
