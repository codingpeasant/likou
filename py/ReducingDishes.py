# https://leetcode.com/problems/reducing-dishes/description/?orderBy=most_votes

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        presum, res = 0, 0
        for i in range(n):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum
        return res


s = Solution()
satisfaction = [-1, -8, 0, 5, -9]
print(s.maxSatisfaction(satisfaction))
