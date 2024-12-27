# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = prev = 0  # index of previously retained letter
        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                ans += min(neededTime[prev], neededTime[i])
                if (
                    neededTime[prev] < neededTime[i]
                ):  # needed because the prev has been moved, prev needs to be updated
                    prev = i
        return ans


s = Solution()
colors = "aaabaaa"
neededTime = [1, 2, 3, 3, 4, 2, 1]
print(s.minCost(colors, neededTime))
