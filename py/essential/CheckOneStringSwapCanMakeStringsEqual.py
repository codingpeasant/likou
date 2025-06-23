# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        countS1, countS2 = Counter(s1), Counter(s2)
        if countS1 != countS2:
            return False

        diffCount = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffCount += 1
            if diffCount > 2:
                return False
        return True


s = Solution()
print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("kelb", "kelb"))
print(s.areAlmostEqual("attack", "defend"))
