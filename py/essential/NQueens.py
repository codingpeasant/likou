# https://leetcode.com/problems/n-queens/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet
# Grind

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        diag1 = set()
        diag2 = set()
        usedCols = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            # try every column
            for col in range(n):
                if col in usedCols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # if it is valid to put a queen here and go to the next row
                board[row][col] = "Q"
                usedCols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                # go to the next row
                backtrack(row + 1)
                board[row][col] = "."
                usedCols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res


s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(10))
