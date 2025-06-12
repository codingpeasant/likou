# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/

from heapq import heappush
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        pq = []
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                heappush(pq, (abs(px - x) + abs(py - y), i))

        return pq[0][1] if pq else -1


s = Solution()
print(s.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
