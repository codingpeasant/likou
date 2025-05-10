# https://leetcode.com/problems/car-pooling/description/
# Neet

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for t in trips:
            stops[t[1]]+=t[0]
            stops[t[2]]-=t[0]
        for i in range(len(stops)):
            capacity-=stops[i]
            if capacity < 0:
                return False
        return capacity >= 0

s=Solution()
print(s.carPooling([[2,1,5],[3,3,7]], 4))
print(s.carPooling([[2,1,5],[3,3,7]], 6))