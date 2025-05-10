# https://leetcode.com/problems/stone-game-ii/description/
# Neet

from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # We define dp[i][m] as the maximum stones Alice can get starting from index i with the current M = m.
        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
        
        return dp[0][1]

s=Solution()
piles = [2, 7, 9, 4, 4]
print(s.stoneGameII(piles))  # Output: 10
piles = [1, 2, 3, 4, 5, 100]
print(s.stoneGameII(piles))  # Output: 104