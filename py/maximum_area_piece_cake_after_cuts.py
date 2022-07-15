# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

from typing import List

# Because we want the maximize the area, we must try to maximize the length and height of each piece. A bit of greedy
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        maxh, maxv = max(hc[0], h - hc[-1]), max(
            vc[0], w - vc[-1]
        )  # first find the max from the edges
        for i in range(len(hc)):  # find the max between 2 adjacent cuts
            maxh = max(maxh, hc[i] - hc[i - 1])
        for i in range(len(vc)):
            maxv = max(maxv, vc[i] - vc[i - 1])
        return (maxh * maxv) % 1000000007


s = Solution()
print(s.maxArea(5, 4, [0], [1]))
