# https://leetcode.com/problems/max-consecutive-ones-iii/description/

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
