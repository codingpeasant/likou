# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res, end = 0, -float("inf")
        points = sorted(points, key=lambda x: x[1])
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res


s = Solution()
points = [[-1, 1], [0, 1], [2, 3], [1, 2]]
print(s.findMinArrowShots(points))
