# https://leetcode.com/problems/permutations-ii/description/
# Neet

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(cur: List[int], updatedNums: List[int]):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(updatedNums)):
                if i > 0 and updatedNums[i] == updatedNums[i - 1]:
                    continue
                backtrack(cur + [updatedNums[i]], updatedNums[:i] + updatedNums[i + 1 :]) # remove the current

        backtrack([], nums)
        return res


s = Solution()
print(s.permuteUnique([1, 2, 3]))
print(s.permuteUnique([1, 1, 3]))
