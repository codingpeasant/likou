# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canEatAll(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
            return hours <= h

        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        return right


s = Solution()
piles = [3, 6, 7, 11]
h = 8
print(s.minEatingSpeed(piles, h))
