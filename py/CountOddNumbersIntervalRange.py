# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1 and low % 2 == 1:
            return int((high - low) / 2 + 1)
        return math.ceil((high - low) / 2)


s = Solution()
print(s.countOdds(7, 10))
