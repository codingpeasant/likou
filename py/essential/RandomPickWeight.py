# https://leetcode.com/problems/random-pick-with-weight/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        # 1. calculate relative frequency
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        # 2. put relative frequencies on the number line between 0 and 1
        # Note self.w[-1] = 1
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]
        print(self.w)

    def pickIndex(self) -> int:
        # this is where we pick the index
        N = random.uniform(0, 1)
        print(N)
        flag = True
        index = -1

        # test each region of the numberline to see if N falls in it, if it
        # does not then go to the next index and check if N falls in it
        # this is guaranteed to break because of previous normalization
        while flag:
            index += 1
            if N <= self.w[index]:
                flag = False
        return index


s = Solution([3, 1])
print(s.pickIndex())
