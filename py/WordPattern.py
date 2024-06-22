# https://leetcode.com/problems/word-pattern/
# Hash Table

from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pToW, wToP, words = defaultdict(str), defaultdict(str), s.split()

        if len(pattern) != len(words):
            return False

        for i, letter in enumerate(pattern):
            if pToW[letter] and words[i] != pToW[letter]:
                return False
            pToW[letter] = words[i]

            if wToP[words[i]] and wToP[words[i]] != letter:
                return False
            wToP[words[i]] = letter
        return True


so = Solution()
pattern = "jqeury"
s = "jquery"
print(so.wordPattern(pattern, s))
