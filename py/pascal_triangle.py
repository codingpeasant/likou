# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for row in range(2, numRows):
            res.append([1] * (row + 1))
            for c in range(1, row):  # first and last element are 1
                res[row][c] = res[row - 1][c] + res[row - 1][c - 1]
        return res


s = Solution()
print(s.generate(5))
