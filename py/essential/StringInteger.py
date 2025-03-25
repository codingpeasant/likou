# https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=rab78cw1
# Grind


class Solution:
    def myAtoi(self, s: str) -> int:
        n, i, sign, res = len(s), 0, 1, 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] in ["+", "-"]:
            sign = 1 if s[i] == "+" else -1
            i += 1

        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        return max(-(2**31), min(sign * res, 2**31 - 1))


s = Solution()
print(s.myAtoi("   -14245"))
