# https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind
# Neet

from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def getMin(curAmount: int) -> int:
            if curAmount < 0:
                return -1
            if curAmount == 0:
                return 0

            curMin = float("inf")
            for coin in coins:
                subMin = getMin(curAmount - coin)
                if subMin == -1:
                    continue
                curMin = min(curMin, subMin + 1)
            return curMin

        amountMin = getMin(amount)
        return amountMin if amountMin != float("inf") else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for subAmount in range(1, amount + 1):
            for j in range(len(coins)):
                if subAmount == coins[j]:
                    dp[subAmount] = 1
                if subAmount - coins[j] > 0:
                    dp[subAmount] = min(
                        dp[subAmount], dp[subAmount - coins[j]] + 1
                    )  # pick the current coin[j] + the min of the rest (i - coins[j])
        return dp[-1] if dp[-1] != float("inf") else -1


s = Solution()
print(s.coinChange([2, 5, 1], 3))
print(s.coinChange1([2, 5, 1], 3))
