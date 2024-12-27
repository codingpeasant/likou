# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n, res = len(strs), len(strs[0]), 0

        for j in range(n):
            for i in range(m - 1):
                if strs[i + 1][j] < strs[i][j]:
                    res += 1
                    break
        return res


s = Solution()
strs = ["a", "b"]
print(s.minDeletionSize(strs))
