# https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, curMax, countMap = -1, 0, Counter(nums)
        for num, count in countMap.items():
            if count > curMax:
                res = num
                curMax = count

        return res

    def majorityElement1(self, nums: List[int]) -> int:
        res, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                res = nums[i]
            elif res == nums[i]:
                count += 1
            else:
                count -= 1

        return res


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement1([6, 5, 5]))
