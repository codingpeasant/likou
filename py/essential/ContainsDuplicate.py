# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
