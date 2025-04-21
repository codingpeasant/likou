# https://neetcode.io/problems/meeting-schedule
# Blind
# Neet
# Grind

from collections import defaultdict
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


s = Solution()
print(s.canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
