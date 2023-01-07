# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

from collections import defaultdict
from functools import lru_cache


class Solution:
    # O(n*k*target)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dfs(cur, index) -> int:
            if cur > target:
                return 0
            if index == n:
                if cur == target:
                    return 1
                else:
                    return 0
            res = 0
            for i in range(1, k + 1):
                res += dfs(cur + i, index + 1)
            return res

        def dp() -> int:
            # row: ith dice; col: value get
            dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
            dp[0][0] = 1
            for i in range(1, n + 1):
                for j in range(1, target + 1):
                    for kth in range(1, k + 1):
                        dp[i][j] = dp[i][j] + (dp[i - 1][j - kth] if kth <= j else 0)
            return dp[n][target] % (10**9 + 7)

        # return dfs(0, 0) % (10**9 + 7)
        return dp()


s = Solution()
print(s.numRollsToTarget(3, 6, 10))
