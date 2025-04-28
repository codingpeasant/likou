# https://leetcode.com/problems/find-in-mountain-array/description/
# Neet


class Solution:
    def findInMountainArray(self, target: int, mountainArr: list) -> int:
        # Binary search to find the peak of the mountain
        left, right = 0, len(mountainArr) - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr[mid] < mountainArr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        peak = left

        # Binary search in the increasing part of the mountain
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountainArr[mid] == target:
                return mid
            elif mountainArr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search in the decreasing part of the mountain
        left, right = peak + 1, len(mountainArr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mountainArr[mid] == target:
                return mid
            elif mountainArr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


s = Solution()
print(s.findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]))
print(s.findInMountainArray(3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
