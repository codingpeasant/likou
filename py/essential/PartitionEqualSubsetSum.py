# https://leetcode.com/problems/partition-equal-subset-sum/?envType=problem-list-v2&envId=rab78cw1
# Grind

from typing import List


class Solution:
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


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
