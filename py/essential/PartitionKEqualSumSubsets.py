# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
# Neet

from functools import lru_cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numSum = sum(nums)
        if numSum % k != 0:
            return False
        subsetSum = numSum / k

        kSums = [0] * k  # track the sum of each subset
        nums.sort(
            reverse=True
        )  # quickly return False if nums[i] is larger than subsetSum

        def backtrack(i):  # similar with match stick problem
            print(kSums)
            if i >= len(nums):
                return True if all(kSum == subsetSum for kSum in kSums) else False

            for j in range(k):
                if kSums[j] + nums[i] <= subsetSum:
                    kSums[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    kSums[j] -= nums[i]
            return False

        return backtrack(0)


s = Solution()
print(
    s.canPartitionKSubsets(
        [
            3522,
            181,
            521,
            515,
            304,
            123,
            2512,
            312,
            922,
            407,
            146,
            1932,
            4037,
            2646,
            3871,
            269,
        ],
        5,
    )
)
