# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Grind

from bisect import bisect_left, bisect_right
from functools import lru_cache
from typing import List


# Let create jobs array which zip startTime, endTime, profit together.
# Let sort our jobs in increasing order of startTime.
# Let dp[i] denote the maximum profit taking jobs in jobs[i...n-1] such that there is no overlapping time range.
# For the current jobs[i], we have 2 choice
# Don't pick ith job: dp(i+1)
# Pick ith job: We earn profit[i] and the next job must have the startTime >= arr[i].endTime to avoid time overlapping.
# So we have to find j from [i+1, n] so that arr[j].startTime >= arr[i].endTime
# Then we have choice dp(j) + profit[i].
# Choose the choice which leads maximum profits between 2 above choices.
# Finally, dp(0) is our result.
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        @lru_cache
        def dp(i: int) -> int:
            if i >= n:
                return 0

            j = bisect_left(
                startTime, jobs[i][1]
            )  # Find the next job that starts after the current job ends
            print(f"{i} - {j}")
            return max(dp(i + 1), dp(j) + jobs[i][2])

        return dp(0)

    # TLE
    def jobScheduling1(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = max(dp[i], jobs[i - 1][2])
            for j in range(i - 1, -1, -1):
                if jobs[j][1] <= jobs[i - 1][0]:
                    dp[i] = max(dp[i], dp[j + 1] + jobs[i - 1][2])

        return max(dp)


s = Solution()
print(s.jobScheduling2([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
print(s.jobScheduling2([1, 1, 1], [2, 3, 4], [5, 6, 4]))
print(
    s.jobScheduling2(
        [6, 15, 7, 11, 1, 3, 16, 2],
        [19, 18, 19, 16, 10, 8, 19, 8],
        [2, 9, 1, 19, 5, 7, 3, 19],
    )
)
