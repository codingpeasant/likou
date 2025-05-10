# https://leetcode.com/problems/stone-game-iii/submissions/957972523/
# Neet


from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] means, if we ignore before A[i],
        # what's the highest score that Alex can win over the Bob？
        # Take A[i], win take - dp[i+1]
        # Take A[i] + A[i+1], win take - dp[i+2]
        # Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]
        # dp[i] equals the best outcome of these three solutions.
        @cache
        def dp(l):
            if l >= n:
                return 0
            max_score = -1001
            R = min(l + 3, n) + 1
            for r in range(l + 1, R):
                score = sum(stoneValue[l:r]) - dp(r)
                max_score = max(max_score, score)

            return max_score

        winners = ["Tie", "Alice", "Bob"]
        score = max(-1, min(dp(0), 1))
        return winners[score]


s = Solution()
print(s.stoneGameIII([1, 2, 3, 7]))
