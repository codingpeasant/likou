# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroCountSoFar, res = 0, 0
        for num in nums:
            if num:
                res += (zeroCountSoFar + 1) * zeroCountSoFar // 2
                zeroCountSoFar = 0
            else:
                zeroCountSoFar += 1
        res += (zeroCountSoFar + 1) * zeroCountSoFar // 2
        return res


s = Solution()
nums = [0, 0, 0, 2, 0, 0]
print(s.zeroFilledSubarray(nums))
