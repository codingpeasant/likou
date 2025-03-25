# https://leetcode.com/problems/distinct-subsequences/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1  # t is empty string

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j]  # if current character s[i] is skipped
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]  # if current character is used

        return dp[-1][-1]


so = Solution()
s = "rabbbit"
t = "rabbit"
print(so.numDistinct(s, t))
