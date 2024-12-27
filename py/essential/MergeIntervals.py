# Blind
# https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res, prevInterval = [], intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prevInterval[1]:
                prevInterval[1] = max(
                    prevInterval[1], intervals[i][1]
                )  # extend the right
            else:
                res.append(prevInterval)
                prevInterval = intervals[i]
        res.append(prevInterval)
        return res


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
