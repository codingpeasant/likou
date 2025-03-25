# https://leetcode.com/problems/edit-distance/
# Neet

from functools import lru_cache


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return j  # Need to insert j chars
            if j == 0:
                return i  # Need to delete i chars
            if s1[i - 1] == s2[j - 1]:
                return dp(i - 1, j - 1)
            return (
                min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
            )  # insert 1 char on s1, delete 1 char on s2, replace s1[i-1] with s2[j-1]

        return dp(len(s1), len(s2))

    def minDistance1(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            dp[i][0] = i  # Need to delete i chars
        for j in range(len(s2) + 1):
            dp[0][j] = j
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[len(s1)][len(s2)]


s = Solution()
word1 = "intention"
word2 = "execution"
print(s.minDistance(word1, word2))
print(s.minDistance1(word1, word2))
