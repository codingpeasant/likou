# https://leetcode.com/problems/greatest-common-divisor-of-strings/

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


s = Solution()
str1 = "ABABAB"
str2 = "ABAB"
print(s.gcdOfStrings(str1, str2))
