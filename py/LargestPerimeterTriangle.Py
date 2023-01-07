# https://leetcode.com/problems/largest-perimeter-triangle/

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(2, len(nums)):
            first, second, third = nums[i - 2], nums[i - 1], nums[i]
            if first < second + third:
                return first + second + third
        return 0


s = Solution()
nums = [1, 1, 2]
print(s.largestPerimeter(nums))
