# https://leetcode.com/problems/count-ways-to-build-good-strings/description/

from functools import lru_cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i > high:
                return 0

            count = dfs(i + zero) + dfs(i + one)
            if low <= i <= high:
                count += 1

            return count % mod

        return dfs(0)


s = Solution()
print(s.countGoodStrings(3, 3, 1, 1))
