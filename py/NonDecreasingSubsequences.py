# https://leetcode.com/problems/non-decreasing-subsequences/

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, n = set(), len(nums)

        def dfs(start: int, curList: List[int]):
            if len(curList) >= 2:
                res.add(tuple(curList.copy()))

            for i in range(start, n):
                if not curList or nums[i] >= curList[-1]:
                    curList.append(nums[i])
                    dfs(i + 1, curList)
                    curList.pop()

        dfs(0, [])

        return res


s = Solution()
nums = [4, 6, 7, 7]
print(s.findSubsequences(nums))
