# https://leetcode.com/problems/sudoku-solver/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check if the number is not in the current row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check if the number is not in the current column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check if the number is not in the current 3x3 box
            start_row = row - row % 3
            start_col = col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == num:
                        return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False # No valid number found
            return True

        solve(board)

s=Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)