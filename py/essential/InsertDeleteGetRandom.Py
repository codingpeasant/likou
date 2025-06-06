# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Grind

from collections import defaultdict
import random


class RandomizedSet:
    def __init__(self):
        self.dataMap = defaultdict(
            int
        )  # dictionary, value to index
        self.data = []  # list aka array

    def insert(self, val: int) -> bool:
        if val in self.dataMap:
            return False
        self.dataMap[val] = len(self.data)  # record the index of the value in self.data
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dataMap:
            return False

        lastEle = self.data[-1]
        indexToRemove = self.dataMap[val]
        # swap the last element with the element to be removed
        self.data[indexToRemove] = lastEle
        self.dataMap[lastEle] = indexToRemove
        self.data.pop()
        self.dataMap.pop(val)
        return True

    def getRandom(self) -> int:
        print(self.data)
        return random.choice(self.data)


s = RandomizedSet()
print(s.insert(0))
print(s.insert(1))
print(s.remove(0))
print(s.insert(2))
print(s.remove(1))
print(s.getRandom())
