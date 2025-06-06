# https://leetcode.com/problems/car-pooling/description/
# Neet

from collections import defaultdict
from typing import List


class Solution:
    # Same with meeting room II
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stopsPeopleCount = defaultdict(int)
        for t in trips:
            stopsPeopleCount[t[1]] += t[0]
            stopsPeopleCount[t[2]] -= t[0]
        for stop in sorted(stopsPeopleCount.keys()):
            capacity -= stopsPeopleCount[stop]
            if capacity < 0:
                return False
        return capacity >= 0


s = Solution()
print(s.carPooling([[2, 1, 5], [3, 3, 7]], 4))
print(s.carPooling([[2, 1, 5], [3, 3, 7]], 6))
