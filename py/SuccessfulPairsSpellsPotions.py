# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

import bisect
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        return [
            len(potions) - bisect.bisect_left(potions, (success + s - 1) // s)
            for s in spells
        ]


s = Solution()
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
print(s.successfulPairs(spells, potions, success))
