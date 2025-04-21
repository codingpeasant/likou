# https://leetcode.ca/2017-12-28-759-Employee-Free-Time/
# Grind

from typing import List


class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        # Flatten the schedule
        flattened = []
        for employee in schedule:
            for interval in employee:
                flattened.append(interval)

        # Sort the intervals by start time
        flattened.sort(key=lambda x: x[0])

        # Merge overlapping intervals - See Merge Intervals
        merged = []
        for interval in flattened:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Find free time between merged intervals
        free_time = []
        for i in range(1, len(merged)):
            free_time.append([merged[i - 1][1], merged[i][0]])

        return free_time


s = Solution()
print(s.employeeFreeTime([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))
