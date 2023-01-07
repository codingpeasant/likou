# https://leetcode.com/problems/jump-game-vi/

import heapq
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = []  # max heap
        val = 0
        for i in range(n):
            maxV = 0
            if queue:
                maxV, indx = queue[0]  # get the largest
                while indx + k < i:  # have to pick the recent k
                    maxV, indx = heapq.heappop(queue)
                heapq.heappush(queue, [maxV, indx])
            val = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * val, i])
        return val


s = Solution()
nums = [-1, -1, -2, -4, -7, 0]
print(s.maxResult(nums, 2))
