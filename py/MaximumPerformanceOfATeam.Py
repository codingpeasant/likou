# https://leetcode.com/problems/maximum-performance-of-a-team/

import heapq
from typing import List

"""
For the PriorityQueue solution, a trick is that each time when you add a new engineer and then lay off the engineer with the least speed, it could be the newly added one. So the new res of the second parameter of Math.max is actually incorrect!

res = max(res, speed_sum * e)

However, in this case the new res value will be definitely lower than the existing res, so it does not matter.

So in this solution you may get an incorrect intermediate result but it doesn't hurt
greedy
"""


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        workers_queue = []
        res = speed_sum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):  # efficiency high to low
            heapq.heappush(workers_queue, s)
            speed_sum += s
            if len(workers_queue) > k:
                speed_sum -= heapq.heappop(workers_queue)
            res = max(res, speed_sum * e)
        return res % (10**9 + 7)


s = Solution()
n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2

print(s.maxPerformance(n, speed, efficiency, k))
