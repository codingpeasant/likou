# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return []
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


s = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(s.kClosest(points, k))
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(s.kClosest(points, k))
