# https://leetcode.com/problems/plus-one/?envType=problem-list-v2&envId=rr2ss0g5

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n - 1, -1, -1):
            curSum = digits[i] + carry
            if curSum == 10:
                carry = 1
                curSum = 0
            else:
                carry = 0
            digits[i] = curSum
        if carry == 1:
            digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9, 9]))
print(s.plusOne([7, 9, 9]))
