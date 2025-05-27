# https://leetcode.com/problems/sudoku-solver/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    rows[i].add(cur)
                    cols[j].add(cur)
                    k = (i // 3) * 3 + j // 3
                    grid[k].add(cur)
        def is_valid(board, row, col, num):
            k = (row // 3) * 3 + col // 3
            if num in rows[row] or num in cols[col] or num in grid[k]:
                return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                rows[i].add(num)
                                cols[j].add(num)
                                k = (i // 3) * 3 + j // 3
                                grid[k].add(num)
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                                rows[i].remove(num)
                                cols[j].remove(num)
                                grid[k].remove(num)
                        return False # No valid number found
            return True

        solve(board)

s=Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)