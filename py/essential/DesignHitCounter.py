# https://leetcode.ca/2016-11-26-362-Design-Hit-Counter/
# Grind


from typing import Counter


# a part of rate limit
class HitCounter:  # extra o(N) space
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = Counter()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum([v for t, v in self.counter.items() if t + 300 > timestamp])


s = HitCounter()
s.hit(1)
s.hit(2)
s.hit(3)
s.hit(4)
s.hit(5)
print(s.getHits(300))  # 5
