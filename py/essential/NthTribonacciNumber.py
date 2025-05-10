# https://leetcode.com/problems/n-th-tribonacci-number/
# Neet

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)


s = Solution()
print(s.tribonacci(25))
