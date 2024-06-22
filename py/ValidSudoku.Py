# https://leetcode.com/problems/valid-sudoku/
# Matrix,Hash Table

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        grid = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":

                    k = (i // 3) * 3 + j // 3

                    if cur not in rows[i]:
                        rows[i].add(cur)
                    else:
                        return False

                    if cur not in cols[j]:
                        cols[j].add(cur)
                    else:
                        return False

                    if cur not in grid[k]:
                        grid[k].add(cur)
                    else:
                        return False
        return True


s = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(s.isValidSudoku(board))
