# https://leetcode.com/problems/climbing-stairs/
# Blind
# Grind
# Neet

from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2

            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)

    def climbStairs1(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


s = Solution()
print(s.climbStairs(5))
print(s.climbStairs1(5))
