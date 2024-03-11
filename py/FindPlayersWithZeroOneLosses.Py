# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans2 = []
        winners = set(match[0] for match in matches)
        losersWithCount = Counter(match[1] for match in matches)
        losers = set(losersWithCount.keys())

        ans1 = list(winners.difference(losers))

        for loser, count in losersWithCount.items():
            if count == 1:
                ans2.append(loser)

        return [sorted(ans1), sorted(ans2)]


s = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(s.findWinners(matches))
