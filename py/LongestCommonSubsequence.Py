# https://leetcode.com/problems/longest-common-subsequence/description/

from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == m or n == j:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)


s = Solution()
text1 = "abcde"
text2 = "ace"
print(s.longestCommonSubsequence(text1, text2))
