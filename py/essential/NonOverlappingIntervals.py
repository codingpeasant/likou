# https://leetcode.com/problems/non-overlapping-intervals/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda interval: interval[0])
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(
                    prevEnd, intervals[i][1]
                )  # greedily remove the longer one
                count += 1

        return count


s = Solution()
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
