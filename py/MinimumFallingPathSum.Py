# https://leetcode.com/problems/minimum-falling-path-sum/description/

from functools import lru_cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return matrix[i][j]
            if j == 0:
                return matrix[i][j] + min(dfs(i - 1, j), dfs(i - 1, j + 1))
            if j == n - 1:
                return matrix[i][j] + min(dfs(i - 1, j - 1), dfs(i - 1, j))
            return matrix[i][j] + min(
                dfs(i - 1, j), dfs(i - 1, j + 1), dfs(i - 1, j - 1)
            )

        return min(dfs(m - 1, j) for j in range(n))


s = Solution()
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(s.minFallingPathSum(matrix))
