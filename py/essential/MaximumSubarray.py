# https://leetcode.com/problems/maximum-subarray/description/
# Blind
# Grind
# Neet

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, res = 0, nums[0]

        for num in nums:
            if curSum < 0:  # there is no value to add curSum as it decreases the res
                curSum = 0
            curSum += num
            res = max(res, curSum)

        return res


s = Solution()
nums = [5, 4, -1, 7, 8]
print(s.maxSubArray(nums))
