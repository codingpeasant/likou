# https://leetcode.com/problems/detect-squares/description/?envType=problem-list-v2&envId=rr2ss0g5
# Neet

from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = []
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.counts[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for px, py in self.points:
            if (
                px != x and py != y and abs(px - x) == abs(py - y)
            ):  # found the diagonal point
                ans += self.counts[(px, y)] * self.counts[(x, py)]  # another two points
        return ans


s = DetectSquares()
s.add([3, 10])
s.add([11, 2])
s.add([3, 2])
print(s.count([11, 10]))
print(s.count([14, 8]))
s.add([11, 2])
print(s.count([11, 10]))
