# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Blind
# Grind

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bought is the cheapest when a buy decision so far when price moves forward;
        # sold is the max profit when a sell decision so far when price moves forward;
        # because sold only happens after the last best bought (cheapest bought), bought and sold don't have to be a DP array
        bought, sold = (
            float("inf"),
            0,
        )  # we want to find the cheapest bought and max profit that should be larger than 0 if it exists

        for price in prices:
            bought = min(bought, price)  # try to find the cheapest bought so far
            sold = max(
                sold, price - bought
            )  # profit is the current price - last best bought

        return sold


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))
