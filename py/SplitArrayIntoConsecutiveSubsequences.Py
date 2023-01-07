# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

import collections
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = (
            collections.Counter()
        )  # endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
        for i in nums:
            if not left[i]:
                continue
            left[i] -= 1
            if (
                end[i - 1] > 0
            ):  # add a number to the end of a existing consecutive subsequence
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:  #  two following number in the left
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True


s = Solution()
nums = [1, 2, 3, 3, 4, 4, 5, 5]
print(s.isPossible(nums))
