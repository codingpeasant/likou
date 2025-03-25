# https://leetcode.com/problems/last-stone-weight/
# Neet

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minusStones = [-stone for stone in stones]
        heapq.heapify(minusStones)
        while len(minusStones) > 1:
            largest = -heapq.heappop(minusStones)
            secondLargest = -heapq.heappop(minusStones)
            if largest != secondLargest:
                heapq.heappush(minusStones, -(largest - secondLargest))
        return -minusStones[0] if len(minusStones) else 0


s = Solution()
stones = [2, 7, 4, 1, 8, 1]
print(s.lastStoneWeight(stones))
stones = [1, 1, 1, 1]
print(s.lastStoneWeight(stones))
