# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Two Pointers,Binary Search

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            # We want the first element of the middle pair,
            # which should be at an even index if the left part is sorted.
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = (
                    mid  # We didn't find a pair. The single element must be on the left
                )
            else:
                left = (
                    mid + 2
                )  # We found a pair. The single element must be on the right.

        return nums[left]


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
