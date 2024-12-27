# https://leetcode.com/problems/first-unique-character-in-a-string/

from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for i, letter in enumerate(s):
            if s_count[letter] == 1:
                return i
        return -1


s = Solution()
input = "loveleetcode"
print(s.firstUniqChar(input))
