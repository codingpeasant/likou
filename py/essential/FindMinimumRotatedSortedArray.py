# Blind
# Neet
# Grind
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # if you compare mid with left, you cannot identify the pivot
            # e.g. 3,4,5,1,2 vs 1,2,3,4,5 - mid > left
            if nums[mid] > nums[right]:  # pivot is on the right side
                left = mid + 1
            else:
                right = mid  # when it's 5,6,7,0,1,2,4, the mid is the min
        return nums[left]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
