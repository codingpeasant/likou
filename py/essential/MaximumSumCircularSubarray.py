# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
# Neet


from heapq import heappop, heappush
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        minHeap = [(0, -1)]  # (preSum, index)
        preSumSoFar = 0
        res = nums[0]
        for i in range(n * 2): # make sure considering every combination in the circular array
            preSumSoFar += nums[i % n]
            while minHeap and i - minHeap[0][1] > n: # remove the elements that are out of the range
                heappop(minHeap)
            preSumMin = minHeap[0][0]
            res = max(res, preSumSoFar - preSumMin)
            heappush(minHeap, (preSumSoFar, i))
        return res

s=Solution()
nums = [1, -2, 3, -2]
print(s.maxSubarraySumCircular(nums))  # Output: 3
nums = [5, -3, 5]
print(s.maxSubarraySumCircular(nums))  # Output: 10