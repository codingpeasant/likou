# https://neetcode.io/problems/meeting-schedule-ii
# Blind
# Neet

from collections import defaultdict
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startEndCount = defaultdict(int)
        for interval in intervals:
            startEndCount[interval.start] += 1
            startEndCount[interval.end] -= 1
        res, cur = 0, 0
        for time in sorted(startEndCount.keys()):
            cur += startEndCount[time]
            res = max(res, cur)  # find out the max overlap
        return res


s = Solution()
print(s.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
