# https://leetcode.com/problems/n-queens/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def isValid(row, col):
            for i in range(n):
                # same column
                if board[i][col] == "Q":
                    return False
                # left up
                if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == "Q":
                    return False
                # right up
                if row - i >= 0 and col + i < n and board[row - i][col + i] == "Q":
                    return False
            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            # try every column
            for col in range(n):
                if isValid(
                    row, col
                ):  # if it is valid to put a queen here and go to the next row
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return res


s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(10))
