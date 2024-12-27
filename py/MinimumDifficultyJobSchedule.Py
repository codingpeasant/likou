# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from functools import lru_cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def dfs(i, d):  # if start work at ith job with d days left.
            if d == 1:  # if there is only 1 day left
                return max(jobDifficulty[i:])
            res, maxd = float("inf"), 0
            for j in range(
                i, n - d + 1
            ):  # try to finish 1 or more jobs on the current day (d)
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res

        return dfs(0, d)


s = Solution()
jobDifficulty = [6, 5, 4, 3, 2, 1]
d = 2
print(s.minDifficulty(jobDifficulty, d))
