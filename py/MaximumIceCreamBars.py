# https://leetcode.com/problems/maximum-ice-cream-bars/description/

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if coins - cost >= 0:
                res += 1
                coins = coins - cost
            else:
                break
        return res


s = Solution()
costs = [1, 3, 2, 4, 1]
coins = 7
print(s.maxIceCream(costs, coins))
