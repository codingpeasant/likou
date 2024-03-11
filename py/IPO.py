# https://leetcode.com/problems/ipo/description/?orderBy=most_votes

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        heap = []
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap:
                w -= heapq.heappop(heap)
        return w


s = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(s.findMaximizedCapital(k, w, profits, capital))
