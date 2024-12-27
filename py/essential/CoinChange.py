# https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=oizxjoit
# Blind

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


s = Solution()
print(s.coinChange([2, 5], 3))
