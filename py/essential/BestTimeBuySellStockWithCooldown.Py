# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, bought, rest = (
            0,
            float("inf"),
            0,
        )  # At the start, you don't have any stock if you just rest

        for price in prices:
            previousSold = sold
            bought = min(
                bought, price - rest
            )  # need to buy to be the first state, otherwise there won't be sold; bought need to be after rest

            sold = max(sold, price - bought)
            rest = max(rest, previousSold)  # rest can only based on previous sold state
            print(f"bought: {bought}, sold: {sold}, rest: {rest}")

        return max(sold, rest)  # the largest state can be at bought or rest state


s = Solution()
prices = [1, 2, 3, 0, 2]
print(s.maxProfit(prices))
