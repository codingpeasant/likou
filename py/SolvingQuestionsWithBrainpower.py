# https://leetcode.com/problems/solving-questions-with-brainpower/description/

from functools import cache
from typing import List

# For each index i we have 2 options:


# Take pointsi and jump the next brainpoweri indexes
# Skip the current index(do not collect pointsi) and move to the next index
class Solution:
    def mostPoints(self, Q: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(Q):
                return 0
            points, jump = Q[i][0], Q[i][1]
            return max(dp(i + 1), points + dp(i + jump + 1))

        return dp(0)


s = Solution()
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
print(s.mostPoints(questions))
