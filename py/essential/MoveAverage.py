# https://leetcode.ca/2016-11-10-346-Moving-Average-from-Data-Stream/

from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        self.windowSize = size
        self.windowSum = 0.0
        self.data = deque()

    def next(self, val):
        self.windowSum += val
        data = self.data

        if len(data) >= self.windowSize:
            self.windowSum -= data.popleft()
        data.append(val)

        return round(self.windowSum / len(data), 2)


ma = MovingAverage(3)
print(ma.next(1))
print(ma.next(10))
print(ma.next(3))
print(ma.next(5))
