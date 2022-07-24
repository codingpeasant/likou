# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_arr = []
        rst = []
        for num in nums[::-1]:
            idx = bisect_left(sorted_arr, num)
            rst.append(idx)
            sorted_arr.insert(idx, num)

        return rst[::-1]


s = Solution()
nums = [5, 2, 6, 1]
print(s.countSmaller(nums))
