# https://leetcode.com/problems/max-points-on-a-line/description/?orderBy=most_votes

from collections import defaultdict
from typing import List


# Concept: A set of points are on a line each of their pair-wise slopes has the same value.
# For each point, we iterate through all the other points and find the slope with each of the other points
# and store the number of pairs which have the same slope and find the max of the number of points.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return float("inf")
            return (y1 - y2) / (x1 - x2)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i + 1 :]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1


s = Solution()
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(s.maxPoints(points))
