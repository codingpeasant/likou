# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

import heapq
from typing import List


class Solution:
  #     # Heap initialization (element, list_idx, idx)
  # Heap: [(0, 1, 0), (4, 0, 0), (5, 2, 0)]

  # # Popping from this heap will result in returning (0, 1, 0)
  # Heap: [(4, 0, 0), (5, 2, 0)]

  # # After range updates, push the next element in 1st list to heap
  # Heap:  [(4, 0, 0), (5, 2, 0), (9, 1, 1)] 
  # # since it was 9 (bigger than 4 & 5), it goes to the end

  # # Keep doing this until it reaches one of the lists' end (break)
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cur_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0)) 
            cur_max = max(cur_max, nums[i][0]) # always the largest element in the heap
        small = [float('-inf'), float('inf')]
        while heap:
            cur_min, list_idx, i = heapq.heappop(heap)
            if cur_max - cur_min < small[1] - small[0]: # found a smaller range
                small = [cur_min, cur_max]
            if i + 1 < len(nums[list_idx]): # there's a next element in the list
                nxt = nums[list_idx][i + 1] # next element in the list that was popped
                heapq.heappush(heap, (nxt, list_idx, i+1))
                cur_max = max(cur_max, nxt)
            else: # one of the lists is exhausted so we cannot go further and return the current range
                break
        return small
    
s= Solution()
print(s.smallestRange([[1,2,3],[4,5,6],[7,8,9]]))
print(s.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))