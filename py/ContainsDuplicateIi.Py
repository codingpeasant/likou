# https://leetcode.com/problems/contains-duplicate-ii/

from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index = defaultdict(lambda: -1)
        for i in range(len(nums)):
            if value_index[nums[i]] >= 0 and i - value_index[nums[i]] <= k:
                return True
            value_index[nums[i]] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
