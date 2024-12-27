# Blind
# https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, numSum = len(nums) + 1, sum(nums)
        return int(n * (n - 1) / 2 - numSum)


s = Solution()
print(s.missingNumber([3, 0, 1]))
