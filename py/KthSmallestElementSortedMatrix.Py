# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                heappush(max_heap, -matrix[i][j])
                if len(max_heap) > k:
                    heappop(max_heap)
        return -heappop(max_heap)


s = Solution()
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(s.kthSmallest(matrix, k))
