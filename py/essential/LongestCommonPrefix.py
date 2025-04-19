# https://leetcode.com/problems/longest-common-prefix/description/?orderBy=most_votes
# Neet

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = min(strs) # get the alphabetically min
        s2 = max(strs)

        for i, letter in enumerate(s1):
            if letter != s2[i]:
                return s1[:i]
        return s1


s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))
