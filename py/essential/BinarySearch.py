# https://leetcode.com/problems/binary-search/description/
# Grind
# Neet

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


s = Solution()
nums = [2, 5]
target = 5
print(s.search(nums, target))
