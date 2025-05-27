from collections import defaultdict
from typing import List


# Neet
# Blind
# Grind
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in numDict:
                return [numDict[target - num], i]
            numDict[num] = i

        return []


s = Solution()
print(s.twoSum([3, 2, 4], 6))
