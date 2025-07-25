# https://leetcode.com/problems/wildcard-matching/description/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)  # col is p row is s
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] != "*":
                break
            dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = (
                        dp[i - 1][j] or dp[i][j - 1]
                    )  # * is treated as matching empty or matching s[i-1]
        return dp[m][n]


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "*"))
print(s.isMatch("cb", "?a"))
print(s.isMatch("cb", "?b"))
print(s.isMatch("adceb", "*a*b"))
