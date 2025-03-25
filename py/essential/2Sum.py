# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        restToIndex = {}
        for i, num in enumerate(nums):
            if num in restToIndex:
                return [restToIndex[num], i]
            restToIndex[target - num] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
