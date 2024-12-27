# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n <= first:  # reset first if found a smaller one
                first = n
            elif n <= second:  # the second smaller found
                second = n
            else:  # if this is reaches, it means there were already first and second hence a third is current n
                return True
        return False


s = Solution()
nums = [2, 1, 5, 0, 4, 6]
print(s.increasingTriplet(nums))
