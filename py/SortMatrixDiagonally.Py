# https://leetcode.com/problems/sort-the-matrix-diagonally/

import collections
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagnal_dict = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagnal_dict[i - j].append(
                    mat[i][j]
                )  # mat[i][j] on the same diagonal have same value of i - j
        for k in diagnal_dict:
            diagnal_dict[k].sort(reverse=1)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagnal_dict[i - j].pop()
        return mat


s = Solution()
mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(s.diagonalSort(mat))
