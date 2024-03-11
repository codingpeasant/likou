# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curPreSum, minPreSum = float("-inf"), 0, 0

        for num in nums:
            curPreSum += num
            res = max(res, curPreSum - minPreSum)
            minPreSum = min(minPreSum, curPreSum)
        return res


s = Solution()
nums = [5, 4, -1, 7, 8]
print(s.maxSubArray(nums))
