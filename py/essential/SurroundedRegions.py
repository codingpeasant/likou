# https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        def markNotSurrounded(i: int, j: int):
            board[i][j] = "N"
            for d in dirs:
                if (
                    0 <= i + d[0] < m
                    and 0 <= j + d[1] < n
                    and board[i + d[0]][j + d[1]] == "O"
                ):
                    markNotSurrounded(i + d[0], j + d[1])

        # Iterate through the borders and mark all "O" as "N"
        for i in range(m):
            if board[i][0] == "O":
                markNotSurrounded(i, 0)
            if board[i][n - 1] == "O":
                markNotSurrounded(i, n - 1)

        for i in range(n):
            if board[0][i] == "O":
                markNotSurrounded(0, i)
            if board[m - 1][i] == "O":
                markNotSurrounded(m - 1, i)

        # then iterate through the board and flip all "O" to "X" (surrounded) and all "N" to "O" (not surrounded)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"


# Test case
s = Solution()
board = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
s.solve(board)
print(
    board
)  # Expected output: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
