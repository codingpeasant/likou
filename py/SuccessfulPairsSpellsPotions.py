# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# Sorting,Binary Search

import bisect
import math
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

    def successfulPairs1(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort(reverse=True)
        minSpells = [math.ceil(success / portion) for portion in potions]
        return [bisect.bisect_right(minSpells, s) for s in spells]


s = Solution()
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
print(s.successfulPairs(spells, potions.copy(), success))
print(s.successfulPairs1(spells, potions.copy(), success))
