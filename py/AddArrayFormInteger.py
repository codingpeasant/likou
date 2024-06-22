# https://leetcode.com/problems/add-to-array-form-of-integer/description/
# Math

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res, carry, n = [], 0, len(num) - 1

        # only when k > 0 makes sense to res, but num needs to be exhausted
        while k > 0 or n >= 0:
            sum = carry
            if k > 0:
                sum += k % 10
                k //= 10
            if n >= 0:
                sum += num[n]
                n -= 1
            res.append(sum % 10)
            carry = sum // 10  # carry > 0 when sum is larger than 10
        if carry > 0:
            res.append(carry)
        return res[::-1]


s = Solution()
num = [2, 1, 5]
k = 806
print(s.addToArrayForm(num, k))
