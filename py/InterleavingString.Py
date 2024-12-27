# https://leetcode.com/problems/interleaving-string/
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        @lru_cache(None)
        def dfs(i, j, k):
            if i > m - 1 and j > n - 1:  # both s1 and s2 are exhausted
                return True
            if i < m and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                return True
            return False

        return len(s1) + len(s2) == len(s3) and dfs(0, 0, 0)


s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))
