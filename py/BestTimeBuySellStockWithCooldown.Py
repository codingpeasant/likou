# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, bought, rest = 0, -float("inf"), 0

        for price in prices:
            bought = max(
                bought, rest - price
            )  # need to buy to be the first state, otherwise there won't be sold
            rest = max(rest, sold)
            sold = max(sold, bought + price)

        return max(sold, rest)  # sold and rest should always be larger than bought at i


s = Solution()
prices = [1, 2, 3, 0, 2]
print(s.maxProfit(prices))
