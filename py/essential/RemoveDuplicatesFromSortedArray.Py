# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Two Pointers
# Neet
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while fast < len(nums) and slow < len(nums):
            # slow makes sure only one unique element is recorded
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            slow += 1
            if fast < len(nums) and slow < fast:
                nums[slow] = nums[fast]

        return slow


s = Solution()
print(s.removeDuplicates([0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
