# http://leetcode.com/problems/design-an-ordered-stream/description/

from collections import defaultdict
from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.orderS = defaultdict(str)
        self.curP = 1
        self.maxP = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.orderS[idKey] = value
        self.maxP = max(self.maxP, idKey)
        for i in range(self.curP, self.maxP + 1):
            if self.orderS.get(i):
                res.append(self.orderS[i])
                self.curP += 1
            else:
                break
        return res


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
print(obj.insert(4, "dddd"))
print(obj.insert(5, "eeee"))
print(obj.insert(2, "bbbb"))
print(obj.insert(1, "aaaa"))
print(obj.insert(3, "cccc"))
