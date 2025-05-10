# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
# Neet

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)

    def helper(self, nums: List[int], index: int, currValue: int) -> int:
        if index == len(nums):
            return currValue
        # include it in the current subset or exclude it.
        return self.helper(nums, index + 1, currValue ^ nums[index]) + self.helper(
            nums, index + 1, currValue
        )


s = Solution()
print(s.subsetXORSum([1, 2, 3, 4, 5]))
