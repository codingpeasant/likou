# https://leetcode.com/problems/decode-ways/
# Blind
# Neet

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s: str) -> int:
            if not s:
                return 1
            if len(s) == 1:
                return 0 if s == "0" else 1
            if int(s[:2]) < 27:
                if int(s[:2]) < 10:
                    return 0
                return dfs(s[1:]) + dfs(s[2:])
            return dfs(s[1:])

        return dfs(s)

    def numDecodings1(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, n + 1):
            if 1 <= int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
            # another possibility of s[i-1:1] has leading 0 which is not considered
        return dp[n]


s = Solution()
strInput = "106"
print(s.numDecodings(strInput))
print(s.numDecodings1(strInput))
