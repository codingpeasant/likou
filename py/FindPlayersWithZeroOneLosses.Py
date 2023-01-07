# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans1, ans2 = [], []
        winners = set(match[0] for match in matches)
        losersWithCount = Counter(match[1] for match in matches)
        losers = set(losersWithCount.keys())

        for winner in winners:
            if winner not in losers:
                ans1.append(winner)

        for loser, count in losersWithCount.items():
            if count == 1:
                ans2.append(loser)

        return [sorted(ans1), sorted(ans2)]


s = Solution()
matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
print(s.findWinners(matches))
