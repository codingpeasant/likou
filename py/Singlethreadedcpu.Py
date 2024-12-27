# https://leetcode.com/problems/single-threaded-cpu/description/
# Simulation,Sorting

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks by start time
        tasks = sorted(
            [
                (start, task_length, index)
                for index, (start, task_length) in enumerate(tasks)
            ],
            reverse=True,  # add the earliest to the last for pop() to work
        )
        ans = []
        current_time = 0
        heap = []

        while tasks or heap:
            # No more queued tasks; jump ahead to next arrival
            if not heap:
                current_time = max(current_time, tasks[-1][0])

            # Add all tasks that have arrived by the current time
            while tasks and tasks[-1][0] <= current_time:
                start, process_time, task_index = tasks.pop()
                # Heap is ordered by process time and old task index
                heapq.heappush(heap, (process_time, task_index))

            next_task_length, next_task_index = heapq.heappop(heap)
            ans.append(next_task_index)

            # Advance time forward
            current_time += next_task_length

        return ans


s = Solution()
tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
print(s.getOrder(tasks))
