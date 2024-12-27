# https://leetcode.com/problems/jump-game-ii/

from functools import lru_cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumpsToReach, n = [float("inf")] * len(nums), len(nums)
        minJumpsToReach[0] = 0

        for i, num in enumerate(nums):
            for j in range(num + 1):
                minJumpsToReach[i + j] = min(
                    minJumpsToReach[i + j], minJumpsToReach[i] + 1
                )
                if i + j >= n - 1:
                    return minJumpsToReach[i + j]

        return minJumpsToReach[n - 1]

    def jump1(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1

            return min([dfs(j) + 1 for j in range(i-1, -1, -1) if nums[j] >= i - j])

        return dfs(len(nums) - 1)


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump1([2, 3, 1, 1, 4]))
