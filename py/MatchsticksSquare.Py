# https://leetcode.com/problems/matchsticks-to-square/

from collections import Counter
from typing import Deque, List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        possible_side = perimeter / 4

        matchsticks.sort(
            reverse=True
        )  # sort in reverse so if biggest value is greater than possible_side we can return False in backtrack
        sums = [0] * 4

        def backtrack(cur):
            if cur == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == possible_side

            for i in range(4):
                if sums[i] + matchsticks[cur] <= possible_side:
                    sums[i] += matchsticks[cur]
                    if backtrack(cur + 1):
                        return True
                    sums[i] -= matchsticks[cur]

            return False

        return backtrack(0)


s = Solution()
input = [1, 1, 2, 2, 2]
print(s.makesquare(input))
