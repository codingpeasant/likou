# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0  # maximum length of the increasing path found so far

        # DFS function to find the length of the longest increasing path starting from the current cell
        # memoization matrix to store the length of the longest increasing path starting from each cell
        @lru_cache(None)
        def dfs(i, j):
            path = 1  # length of the increasing path starting from the current cell
            for x, y in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]:  # explore all four directions (right, left, down, up)
                if (
                    0 <= i + x < m
                    and 0 <= j + y < n
                    and matrix[i + x][j + y] > matrix[i][j]
                ):  # if the neighbor has a greater value, move to it
                    path = max(
                        path, 1 + dfs(i + x, j + y)
                    )  # update the length of the increasing path

            return path

        for i in range(m):
            for j in range(n):
                res = max(
                    res, dfs(i, j)
                )  # update the maximum length of the increasing path found so far
        return res


s = Solution()
print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))  # 4
