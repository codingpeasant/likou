# https://leetcode.com/problems/smallest-number-in-infinite-set/description/

from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.nextNum = 1
        self.addBackHeap = []
        self.addBackSet = set()

    def popSmallest(self) -> int:
        if self.addBackHeap:
            smallest = heappop(self.addBackHeap)
            self.addBackSet.remove(smallest)
            return smallest

        num_to_return = self.nextNum
        self.nextNum += 1
        return num_to_return

    def addBack(self, num: int) -> None:
        if num < self.nextNum and num not in self.addBackSet:
            self.addBackSet.add(num)
            heappush(self.addBackHeap, num)


s = SmallestInfiniteSet()
print(s.popSmallest())
print(s.popSmallest())
print(s.popSmallest())
print(s.addBack(2))
print(s.popSmallest())
