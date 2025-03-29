# https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
# Test case
s = Solution()
nums = [4, 1, 2, 1, 2]
print(s.singleNumber(nums))  # Output: 4
print(0^5^5)
print(5 << 1)