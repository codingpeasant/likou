# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/

from typing import List
from sortedcontainers import SortedSet


class SummaryRanges:
    def __init__(self):
        self.sortedList = SortedSet()

    def addNum(self, value: int) -> None:
        self.sortedList.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.sortedList:
            return []
        left, right, intervals = -1, -1, []
        for value in self.sortedList:
            if left < 0:  # initial state
                left = right = value
            elif value == right + 1:
                right = value
            else:
                intervals.append([left, right])
                left = right = value
        intervals.append([left, right])
        return intervals


s = SummaryRanges()
s.addNum(1)
print(s.getIntervals())
s.addNum(3)
print(s.getIntervals())
s.addNum(7)
print(s.getIntervals())
s.addNum(2)
print(s.getIntervals())
s.addNum(6)
print(s.getIntervals())
