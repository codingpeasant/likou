# https://leetcode.com/problems/set-mismatch/

from typing import Counter, List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        number_occourance = Counter(nums)
        dup = missing = float("inf")

        for i in range(1, len(nums) + 1):
            if number_occourance[i] == 2:
                dup = i
            if not number_occourance[i]:
                missing = i

        return [dup, missing]


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
