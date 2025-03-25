# https://leetcode.com/problems/coin-change-ii/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:  # different from CoinChange.py
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


s = Solution()
print(s.change(5, [1, 2, 5]))
print(s.change(4, [1, 2, 5]))
print(s.change(3, [1, 2, 5]))
print(s.change(2, [1, 2, 5]))
print(s.change(1, [1, 2, 5]))
