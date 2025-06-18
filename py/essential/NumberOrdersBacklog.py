# http://leetcode.com/problems/number-of-orders-in-the-backlog/description/

from heapq import heappop, heappush
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []  # (-price, amount) and (price, amount)
        for p, a, t in orders:
            if t == 0:
                while a and sell and sell[0][0] <= p:
                    x, y = heappop(sell)
                    if a >= y:
                        a -= y
                    else:
                        heappush(sell, (x, y - a))
                        a = 0
                if a:
                    heappush(buy, (-p, a))
            else:
                while a and buy and -buy[0][0] >= p:
                    x, y = heappop(buy)
                    if a >= y:
                        a -= y
                    else:
                        heappush(buy, (x, y - a))
                        a = 0
                if a:
                    heappush(sell, (p, a))
        mod = 10**9 + 7
        return sum(v[1] for v in buy + sell) % mod


s = Solution()
print(s.getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
