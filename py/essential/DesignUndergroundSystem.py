# https://leetcode.com/problems/design-underground-system/description/

from collections import Counter, defaultdict


class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        self.freqs = Counter()

    def checkIn(self, id, stationName, t):
        self.ids[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        Name2, t2 = self.ids.pop(id)
        self.pairs[(Name2, stationName)] += t - t2
        self.freqs[(Name2, stationName)] += 1

    def getAverageTime(self, startStation, endStation):
        return (
            self.pairs[startStation, endStation] / self.freqs[startStation, endStation]
        )


s = UndergroundSystem()
s.checkIn(1, "A", 1)
s.checkIn(2, "B", 2)
s.checkIn(3, "C", 3)
s.checkOut(1, "D", 4)
s.checkOut(2, "E", 5)
s.checkOut(3, "F", 6)
print(s.getAverageTime("A", "D"))
