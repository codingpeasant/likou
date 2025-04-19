# https://leetcode.com/problems/partition-equal-subset-sum/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from functools import lru_cache
from typing import List


class Solution:
    # starting from a brute force solution which is to find all the subsets and check if any of them sums to target
    # but there is repetition in the subsets, so we can use memoization to speed it up
    # For example, when we know that [1,5] can add up to 6, [1,5,5] is 6 ([1,5]) + 5
    # dp[2][6] = True so dp[3][11 - 5] = True
    def canPartition(self, nums: List[int]) -> bool:
        n, target = len(nums), sum(nums) // 2
        if sum(nums) & 1 == 1:
            return False

        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for numIndex in range(1, n + 1):
            for subTarget in range(target + 1):
                if (
                    nums[numIndex - 1] > subTarget
                ):  # cannot choose this number, use the prev result that adds to subTarget
                    dp[numIndex][subTarget] = dp[numIndex - 1][subTarget]
                else:  # pick or not pick
                    dp[numIndex][subTarget] = (
                        dp[numIndex - 1][subTarget]
                        or dp[numIndex - 1][subTarget - nums[numIndex - 1]]
                    )
                if (
                    subTarget == target and dp[numIndex][subTarget]
                ):  # found a valid one e.g. found 11 or found 1,5,5
                    return True
        return False

    # easier to understand from the brute force solution below
    def canPartition2(self, nums: List[int]) -> bool:
        n, target = len(nums), sum(nums) // 2
        if sum(nums) & 1 == 1:
            return False

        @lru_cache(None)
        def dfs(numIndex: int, subTarget: int) -> bool:
            if subTarget == 0:
                return True
            if numIndex == 0 or subTarget < 0:
                return False
            # pick or not pick
            return dfs(numIndex - 1, subTarget) or dfs(
                numIndex - 1, subTarget - nums[numIndex]
            )

        return dfs(n - 1, target)

    # brute force solution
    def canPartitionBacktrack(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if (
            s % 2 != 0
        ):  # if 's' is a an odd number, we can't have two subsets with equal sum
            return False
        return self.canPartitionHelper(nums, s / 2, 0)

    def canPartitionHelper(self, nums, sum, currentIndex):
        if sum == 0:  # base check
            return True
        numsLen = len(nums)
        if numsLen == 0 or currentIndex >= numsLen:
            return False

        # recursive call after choosing the number at the `currentIndex`
        # if the number at `currentIndex` exceeds the sum, we shouldn't process this
        if nums[currentIndex] <= sum:
            if self.canPartitionHelper(
                nums, sum - nums[currentIndex], currentIndex + 1
            ):
                return True  # Backtrack

        # recursive call after excluding the number at the 'currentIndex'
        return self.canPartitionHelper(nums, sum, currentIndex + 1)


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition2([1, 5, 11, 5]))
print(s.canPartition([1, 5, 11, 6]))
print(s.canPartition2([1, 5, 11, 6]))
