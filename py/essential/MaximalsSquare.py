# https://leetcode.com/problems/maximal-square/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        max_side = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    # in order to expand max_side, the i-1, j-1 and [i-1][j-1] have to satisfy the condition. Otherwise [i][j] can only inherent the smallest one
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


s = Solution()
print(
    s.maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)  # 4
print(s.maximalSquare([["0", "1"], ["1", "0"]]))  # 1
