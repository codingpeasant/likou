# https://leetcode.com/problems/house-robber-ii/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])

        startFirst, startSecond = [0] * (n + 1), [0] * (n + 1)
        startFirst[1] = nums[0]
        startSecond[2] = nums[1]

        for i in range(2, n):
            startFirst[i] = max(startFirst[i - 2] + nums[i - 1], startFirst[i - 1])

        for i in range(3, n + 1):
            startSecond[i] = max(startSecond[i - 2] + nums[i - 1], startSecond[i - 1])

        return max(startFirst[n - 1], startSecond[n])

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])

        def robHouses(nums: List[int]):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        return max(robHouses(nums[:-1]), robHouses(nums[1:]))


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob1([1, 2, 3, 1]))
