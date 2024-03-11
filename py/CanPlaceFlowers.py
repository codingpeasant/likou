# https://leetcode.com/problems/can-place-flowers/description/?orderBy=most_votes

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, flower in enumerate(flowerbed):
            if (
                not flower
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                flowerbed[i] = 1
        return n <= 0


s = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(s.canPlaceFlowers(flowerbed, n))
