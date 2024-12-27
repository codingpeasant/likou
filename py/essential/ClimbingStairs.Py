# https://leetcode.com/problems/climbing-stairs/
# Blind

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


s = Solution()
print(s.climbStairs(5))
