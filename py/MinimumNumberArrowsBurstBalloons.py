# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points = sorted(points, key=lambda x: x[0])
        end = points[0][1]
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
            else:
                end = min(end, interval[1])
        return res


s = Solution()
points = [[-1, 1], [0, 1], [2, 3], [1, 2]]
print(s.findMinArrowShots(points))
print(
    s.findMinArrowShots(
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
    )
)
