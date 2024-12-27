# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/


# If we know the longest palindromic sub-sequence is x and the length of the string is n then, what is the answer to this problem?
# It is n - x as we need n - x insertions to make the remaining characters also palindrome.
# where dp[i][j] means the length of longest common sequence between
# i first letters in s1 and j first letters in s2.
from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        reversedS, n = s[::-1], len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == reversedS[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n - dp[n][n]

    def minInsertions1(self, s: str) -> int:
        reversedS, n = s[::-1], len(s)

        @lru_cache(None)
        def dfs(i, j) -> int:
            if i == 0 or j == 0:
                return 0
            if s[i - 1] == reversedS[j - 1]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return n - dfs(n, n)


s = Solution()
input = "leetcode"
print(s.minInsertions(input))
print(s.minInsertions1(input))
