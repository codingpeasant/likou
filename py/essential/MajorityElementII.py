# https://leetcode.com/problems/majority-element-ii/description/
# Neet

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = 0
        m1, m2 = 0, 1
        for m in nums:
            if m == m1:
                n1 += 1
            elif m == m2:
                n2 += 1
            elif n1 == 0:
                m1, n1 = m, 1
            elif n2 == 0:
                m2, n2 = m, 1
            else:
                n1, n2 = n1 - 1, n2 - 1
        return [m for m in [m1, m2] if nums.count(m) > len(nums) // 3]

    def majorityElement1(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [k for k, v in counter.items() if v > len(nums) // 3]


s = Solution()
nums = [3, 2, 3]
print(s.majorityElement1(nums))
