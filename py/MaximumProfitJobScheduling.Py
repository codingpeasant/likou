# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from bisect import bisect_left, bisect_right
from collections import defaultdict
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
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)), key=lambda v: v[0])

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            ans = dp(i + 1)  # Choice 1: Don't pick

            j = bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
            return ans

        return dp(0)


s = Solution()
print(s.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
