# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            self._addAndRefresh(num)

    def _addAndRefresh(self, val: int):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        self._addAndRefresh(val)
        return self.minHeap[0]


s = KthLargest(3, [4, 5, 8, 2])
print(s.add(3))
print(s.add(10))