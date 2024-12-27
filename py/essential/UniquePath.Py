# https://leetcode.com/problems/unique-paths/
# DP
# Blind


from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]

    def uniquePaths1(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int):
            if i == 0 or j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)

    # TTL
    def uniquePaths2(self, m: int, n: int) -> int:
        self.res = 0

        def dfs(i: int, j: int):
            if i == m - 1 and j == n - 1:
                self.res += 1
            if 0 <= i + 1 < m:
                dfs(i + 1, j)
            if 0 <= j + 1 < n:
                dfs(i, j + 1)

        dfs(0, 0)
        return self.res


s = Solution()
print(s.uniquePaths(10, 7))
print(s.uniquePaths1(10, 7))
print(s.uniquePaths2(10, 7))
