# https://leetcode.com/problems/remove-element/description/
# Neet

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # left
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
input = [0, 1, 2, 2, 3, 0, 4, 2]
print(s.removeElement(input, 2))
print(input)
print(s.removeElement([3, 3, 3, 3], 3))