# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/

from typing import List


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        n = len(capacity)
        if sum(capacity) <= sum(rocks) + additionalRocks:
            return n

        rocksNeeded = sorted([capacity[i] - rocks[i] for i in range(n)])
        for i in range(n):
            while rocksNeeded[i] > 0 and additionalRocks >= rocksNeeded[i]:
                additionalRocks -= rocksNeeded[i]
                rocksNeeded[i] = 0

        return rocksNeeded.count(0)


s = Solution()
capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 1
print(s.maximumBags(capacity, rocks, additionalRocks))
