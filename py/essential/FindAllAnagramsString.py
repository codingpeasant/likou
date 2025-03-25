# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Grind

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        charCount, left, right, res = Counter(p), 0, 0, []
        while right < len(s):
            charCount[s[right]] -= 1
            while charCount[s[right]] < 0:
                charCount[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                res.append(left)
            right += 1
        return res


so = Solution()
s = "cbaebabacd"
p = "abc"
print(so.findAnagrams(s, p))
