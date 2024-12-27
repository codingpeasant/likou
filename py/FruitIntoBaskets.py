# https://leetcode.com/problems/fruit-into-baskets/description/

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        typeCount, left = defaultdict(int), 0

        for right, _ in enumerate(fruits):
            typeCount[fruits[right]] += 1
            if len(typeCount) > 2:
                typeCount[fruits[left]] -= 1
                if typeCount[fruits[left]] == 0:
                    del typeCount[fruits[left]]
                left += 1
        return right - left + 1


s = Solution()
print(s.totalFruit([1, 2, 3, 2, 2]))
