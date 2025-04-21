# https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for right in range(n): # left is first zero
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

nums = [0, 1, 0, 3, 12]
s=Solution()
s.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]