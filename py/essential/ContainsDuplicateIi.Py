# https://leetcode.com/problems/contains-duplicate-ii/
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index = defaultdict(int)
        for i in range(len(nums)):
            if value_index.get(nums[i]) != None and i - value_index[nums[i]] <= k: # seen before and within k distance
                return True
            value_index[nums[i]] = i
        return False

s = Solution()
print(s.containsNearbyDuplicate1([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate1([0, 1, 2, 3, 2, 5], 3))
