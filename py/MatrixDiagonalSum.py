# https://leetcode.com/problems/matrix-diagonal-sum/description/


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res, n = 0, len(mat[0])
        mid = n // 2
        for i in range(n):
            res += mat[i][i]
            res += mat[n - 1 - i][i]

        if n % 2 != 0:
            res -= mat[mid][mid]

        return res


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.diagonalSum(mat))
