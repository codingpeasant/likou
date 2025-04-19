# https://leetcode.com/problems/find-median-from-data-stream/
# Neet

from heapq import *


class MedianFinder:
    def __init__(self):
        self.max_heap = []  # the smaller half of the list, max heap (invert min-heap)
        self.min_heap = []  # the larger half of the list, min heap

    def addNum(self, num: int) -> None:
        # smaller half is equal or larger by 1
        if len(self.max_heap) == len(self.min_heap):
            heappush(
                self.max_heap, -heappushpop(self.min_heap, num)
            )  # first half is larger now
        else:
            heappush(
                self.min_heap, -heappushpop(self.max_heap, -num)
            )  # same length now
        return

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


s = MedianFinder()
s.addNum(1)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())
s.addNum(4)
print(s.findMedian())
