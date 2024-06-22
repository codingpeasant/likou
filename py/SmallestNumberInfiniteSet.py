# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
# Data Structure,Heap

from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.nextNum = 1  # the first number after which all the numbers available
        self.addBackHeap = []
        self.addBackSet = set()  # to prevent dup numbers in the heap

    def popSmallest(self) -> int:
        if self.addBackHeap:  # smaller numbers were added back
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
