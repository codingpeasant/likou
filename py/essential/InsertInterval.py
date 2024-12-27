# https://leetcode.com/problems/insert-interval/
# Blind

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res, toAdd = [], newInterval

        for interval in intervals:
            if toAdd[1] < interval[0]:  # toAdd is before interval
                res.append(toAdd)
                toAdd = interval
            elif (
                toAdd[0] <= interval[1]
            ):  # toAdd[1] could be shorter than interval[1] or longer, so not adding to res yet
                toAdd = [min(interval[0], toAdd[0]), max(interval[1], toAdd[1])]
            else:  # toAdd the after interval
                res.append(interval)
        res.append(toAdd)
        return res


s = Solution()
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(s.insert(intervals, newInterval))
