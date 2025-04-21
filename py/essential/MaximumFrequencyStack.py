# http://leetcode.com/problems/maximum-frequency-stack/description/?envType=problem-list-v2&envId=rabvlt31
# Grind


from collections import defaultdict
from heapq import heappop, heappush


class FreqStack:
    def __init__(self):
        self.heap = []
        self.dict = defaultdict(int)
        self.indexPosition = 0

    def push(self, x: int) -> None:
        self.indexPosition += (
            1  # represents the order in which we push elements in the stack
        )
        self.dict[x] += 1
        heappush(
            self.heap, [-self.dict[x], -self.indexPosition, x]
        )  # push frequency, position and element in the queue

    def pop(self) -> int:
        largest = heappop(self.heap)
        self.dict[largest[2]] -= 1  # largest[2] == element
        return largest[2]


s = FreqStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
s.push(3)
s.push(3)
print(s.pop())  # 3
print(s.pop())  # 3
print(s.pop())  # 2
print(s.pop())  # 3
print(s.pop())  # 2
print(s.pop())  # 1
