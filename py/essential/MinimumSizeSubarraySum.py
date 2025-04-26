# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Neet

from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        curSum = 0
        res = inf
        while right < len(nums):
            curSum += nums[right]
            while curSum >= target:
                res = min(res, right - left + 1)
                curSum -= nums[left]
                left += 1
            right += 1
        return res if res < inf else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
