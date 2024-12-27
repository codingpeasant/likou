# Blind
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=oizxjoit


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res, n = -1, len(nums)

        def findSmallestIndex():
            left, right = 0, n - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return left

        smallestIndex = findSmallestIndex()
        if nums[smallestIndex] == target:
            return smallestIndex
        left = 0
        right = n - 1
        if nums[right] > target:
            left = smallestIndex + 1
        elif nums[right] < target:
            right = smallestIndex - 1
        else:
            return right

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 7))
