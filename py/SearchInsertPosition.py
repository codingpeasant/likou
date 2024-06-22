# https://leetcode.com/problems/search-insert-position/description/
# Binary Search

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # target might be put at index n

        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:  # bisect left
                left = mid + 1
            else:
                right = mid

        return left


s = Solution()
nums = [1, 3, 5, 6]
target = 7
print(s.searchInsert(nums, target))
