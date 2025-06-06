# https://leetcode.com/problems/perfect-squares/
# Neet

from functools import lru_cache
from typing import Annotated


class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num: int) -> int:
            if num <= 3:
                return num
            return min(dfs(num - i * i) for i in range(int(num**0.5), 0, -1)) + 1

        return dfs(n)

    def numSquaresDP(self, n: int) -> int:
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i**0.5) + 1)) + 1
        return dp[n]

    # this is wrong
    @lru_cache(None)
    def numSquaresBF(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.numSquaresBF(n - int(n**0.5) ** 2) + 1


s = Solution()
print(s.numSquares(12))
print(s.numSquaresDP(12))
print(s.numSquaresBF(12))
