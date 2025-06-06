# https://leetcode.com/problems/integer-break/description/
# Neet


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = -float("inf")
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i - j]) # break n into 2 or more than 2
        print(dp[1:7])
        return dp[n]


s = Solution()
print(s.integerBreak(10))
