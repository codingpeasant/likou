# https://leetcode.com/problems/n-queens-ii/description/
# Neet

from typing import Set


class Solution:
    def totalNQueens(self, n):        
        diag1 = set()
        diag2 = set()
        usedCols = set()
        
        return self.helper(n, diag1, diag2, usedCols, 0)

    def helper(self, n, diag1: Set[int], diag2: Set[int], usedCols: Set[int], row):
        if row == n:
            return 1
        
        solutions = 0
        
        # for each row, try each col
        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in usedCols:
                continue
            
            diag1.add(row + col) # bottom left to up right
            diag2.add(row - col) # up left to bottom right
            usedCols.add(col)
            
            solutions += self.helper(n, diag1, diag2, usedCols, row + 1)
        
            diag1.remove(row + col)
            diag2.remove(row - col)
            usedCols.remove(col)
        
        return solutions
        
s=Solution()
print(s.totalNQueens(10))