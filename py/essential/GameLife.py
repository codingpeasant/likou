# https://leetcode.com/problems/game-of-life/description/

from collections import deque
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                live = 0
                for x, y in directions:
                    if (
                        (i + x < len(board) and i + x >= 0)
                        and (j + y < len(board[0]) and j + y >= 0)
                        and abs(board[i + x][j + y]) == 1  # -1 or 1
                    ):
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1  # prev is 1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if (board[i][j] > 0) else 0


s = Solution()
input = [[0, 1, 0], [1, 0, 1], [0, 0, 0]]
s.gameOfLife(input)
print(input)
