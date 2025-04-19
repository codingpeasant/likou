# https://leetcode.com/problems/roman-to-integer/
# String,Math
# Grind


class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0

        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


s = Solution()
str = "MCMXCIV"
print(s.romanToInt(str))
