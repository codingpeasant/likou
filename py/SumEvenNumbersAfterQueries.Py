# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

from tkinter import E
from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = []
        even_total = sum(num for num in nums if num % 2 == 0)

        for val, index in queries:
            prev = nums[index]
            nums[index] += val
            if prev % 2 == 0 and val % 2 == 0:
                even_total += val
            elif prev % 2 == 0 and val % 2 != 0:
                even_total -= prev
            elif prev % 2 != 0 and val % 2 != 0:
                even_total += nums[index]
            res.append(even_total)
        return res


s = Solution()
nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(s.sumEvenAfterQueries(nums, queries))
