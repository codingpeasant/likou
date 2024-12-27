# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set, num2Set = set(nums1), set(nums2)
        return [list(num1Set.difference(num2Set)), list(num2Set.difference(num1Set))]


s = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(s.findDifference(nums1, nums2))
