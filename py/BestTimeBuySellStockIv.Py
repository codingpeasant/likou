# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from math import inf
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n / 2:  # fast case as we can buy and sell every single day
            max_profit = 0
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]
                if profit > 0:
                    max_profit += profit
            return max_profit

        # sell is all 0 (don't buy or sell at all);
        buy = [inf] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                buy[i] = min(
                    buy[i], price - sell[i - 1]
                )  # find the min to make the next buy after selling the previous
                sell[i] = max(
                    sell[i], price - buy[i]
                )  # max the profit if sell here the ith time - worst case sell[i] == sell[i] previous transaction

        return sell[k]


s = Solution()
k = 2
prices = [3, 2, 6, 5, 0, 3]
print(s.maxProfit(k, prices))
