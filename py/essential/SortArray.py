# https://leetcode.com/problems/sort-an-array/description/
# Sorting
# Neet

import random
from typing import List


class Solution:
    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.sortArray(lt) + eq + self.sortArray(gt)


s = Solution()
nums = [5, 1, 1, 2, 0, 0]
print(s.sortArray(nums))
