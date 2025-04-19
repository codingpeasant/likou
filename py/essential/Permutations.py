# https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from typing import List


class Solution:
    # time complexity: O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(curNums: list):
            if len(curNums) == n:
                res.append(curNums.copy())
            for num in nums:
                if not num in curNums:
                    backtrack(curNums + [num])

        backtrack([])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
