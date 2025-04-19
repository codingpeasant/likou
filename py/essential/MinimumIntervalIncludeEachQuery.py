# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/?envType=problem-list-v2&envId=plakya4j
# Neet

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # we must sort the intervals and queries to be able to skip the used smaller intervals so speed up, rather than scanning all the intervals for each query
        queries_asc = sorted((q, i) for i, q in enumerate(queries))
        intervals.sort()
        
        i, num_intervals = 0, len(intervals)
        size_heap = [] # (size, left)
        
        for qnum, pos in queries_asc:
            while i < num_intervals:
                left, right = intervals[i]
                if left > qnum:
                    break
                heapq.heappush(size_heap, (right - left + 1, left)) # get all the intervals that start before or at qnum
                i += 1
            
            while size_heap:
                size, left = size_heap[0]
                right = left + size - 1
                if right >= qnum: # the first interval in the heap is the smallest one that contains qnum
                    break
                heapq.heappop(size_heap) # we don't need this interval anymore or the next iteration because the following qnum are larger than it
                   
            queries[pos] = size_heap[0][0] if size_heap else -1
        
        return queries
    
s=Solution()
print(s.minInterval([[1,4],[2,4],[3,6]], [2,3,4,5])) # [3,3,3,4]