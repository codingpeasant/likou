# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Neet

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if set(str1) != set(str2):
            return ""
        if len(str1) > len(str2):
            if not str1.startswith(str2) or not str1.endswith(str2):
                return ""
        else:
            if not str2.startswith(str1) or not str2.endswith(str1):
                return ""
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


s = Solution()
str1 = "ABABAB"
str2 = "ABAB"
print(s.gcdOfStrings(str1, str2))
