# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        charCount, left, res = Counter(p), 0, []
        for right, char in enumerate(s):
            charCount[char] -= 1  # Counter returns defaultdict(int)
            while charCount[char] < 0:
                charCount[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                res.append(left)
        return res


so = Solution()
s = "cbaebabacd"
p = "abc"
print(so.findAnagrams(s, p))
