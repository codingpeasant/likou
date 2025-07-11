# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/

from functools import lru_cache

# Let dp is the minimum cost for make sure we win in range [l, r] (inclusive).
# If we choose i and wrong, the correct answer should be in [l, i - 1] or [i + 1, r]. So if we choose i and wrong, we need to get maximum cost between this 2 cases + i for make sure we always win even the correct answer in [l, i - 1] or [i + 1, r].
# So minimum cost for make sure we win if we choose i and wrong is i + max(dp(l, i - 1), dp(i + 1, r)).
# Try all possible i in range [l, r] and find the minimum to get the minimum cost for make sure we win in range [l, r].

# The DP function dp(l, r) is called for all pairs (l, r) where 1 ≤ l ≤ r ≤ n.
# There are O(n²) such pairs.
# For each pair, the inner loop tries all possible i in [l, r), which is O(n) work.
# So, total time complexity is O(n²) * O(n) = O(n³).


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(l, r):
            if l >= r:
                return 0  # just guess l or r and it must be right so pay 0
            ans = float("inf")
            for i in range(l, r):
                ans = min(ans, max(dp(l, i - 1), dp(i + 1, r)) + i)
            return ans

        return dp(1, n)


s = Solution()
print(s.getMoneyAmount(10))
