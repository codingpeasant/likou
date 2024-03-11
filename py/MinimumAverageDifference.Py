# https://leetcode.com/problems/minimum-average-difference/

import math
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        preSum, minIndex, minAve, totalSum = [0] * len(nums), 0, float("inf"), sum(nums)
        for i, num in enumerate(nums):
            preSum[i] = preSum[i - 1] + num if i != 0 else num

            secondHalfAve = (
                (totalSum - preSum[i]) // (len(nums) - i - 1)
                if i < len(nums) - 1
                else 0
            )
            averageDiff = abs(preSum[i] // (i + 1) - secondHalfAve)
            if minAve > averageDiff:
                minAve = averageDiff
                minIndex = i
        return minIndex


s = Solution()
nums = [0, 1, 0, 1, 0, 1]
print(s.minimumAverageDifference(nums))
