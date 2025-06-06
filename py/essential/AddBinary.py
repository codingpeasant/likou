# https://leetcode.com/problems/add-binary/
# Math
# Grind


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry, m, n = [], 0, len(a) - 1, len(b) - 1

        while m >= 0 or n >= 0:
            if m >= 0:
                carry += int(a[m])
                m -= 1
            if n >= 0:
                carry += int(b[n])
                n -= 1
            res.append(carry % 2)
            carry = carry // 2
        if carry > 0:
            res.append(carry)
        return "".join(str(num) for num in res[::-1])


s = Solution()
print(s.addBinary("11", "1"))
