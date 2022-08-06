# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        def find_first():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def find_second():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if right < 0 or nums[right] != target:
                return -1
            return right

        res.append(find_first())
        res.append(find_second())

        return res


s = Solution()

nums = [5, 7, 7, 8, 8, 10]
target = 8

print(s.searchRange(nums, target))
