# https://leetcode.com/problems/longest-common-subsequence/description/
# Blind
# Neet

from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i - 1, j - 1)
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(m - 1, n - 1)
    
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Initializing a 2D array for dynamic programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Filling up the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the DP array
        return dp[m][n]


s = Solution()
text1 = "abcde"
text2 = "ace"
print(s.longestCommonSubsequence(text1, text2))
print(s.longestCommonSubsequence1(text1, text2))
