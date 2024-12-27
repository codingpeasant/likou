# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
# Heap,Greedy

import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        sortedPiles = []
        for pile in piles:
            heapq.heappush(sortedPiles, -pile)
        for _ in range(k):
            largest = -heapq.heappop(sortedPiles)
            heapq.heappush(sortedPiles, -largest // 2)

        return -sum(sortedPiles)


s = Solution()
piles = [4, 3, 6, 7]
k = 3
print(s.minStoneSum(piles, k))
