# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from functools import lru_cache
from typing import List


# dp[i,k] means the max value picking k elements from pile[i] to pile[n-1].
# We can pick 0,1,2,3... elements from the current pile[i] one by one.
# It asks for the maximum total value of coins we can have,
# so we need to return max of all the options.
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @lru_cache(None)
        def dfs(i, k):
            if i == n or k == 0:
                return 0
            res, cur = (
                dfs(i + 1, k),
                0,
            )  # first get the max value picking k from next piles
            for j in range(
                min(k, len(piles[i]))
            ):  # pick k or all the coins from the current pile i
                cur += piles[i][j]
                res = max(
                    res, cur + dfs(i + 1, k - j - 1)
                )  # state transition from previous states and find the max
            return res

        return dfs(0, k)

    def maxValueOfCoins1(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @lru_cache(None)
        def dfs(i, k):
            if i < 0 or k == 0:
                return 0
            if i == 0:  # not necessary but clearer to have
                return sum(piles[i][: min(k, len(piles[i]))])
            res, cur = (
                dfs(i - 1, k),
                0,
            )
            for j in range(min(k, len(piles[i]))):
                cur += piles[i][j]
                res = max(res, cur + dfs(i - 1, k - (j + 1)))
            return res

        return dfs(n - 1, k)


s = Solution()
piles = [[1, 100, 3], [7, 8, 9]]
k = 2
print(s.maxValueOfCoins(piles, k=k))
print(s.maxValueOfCoins1(piles, k=k))
