# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Counter, word2Counter = Counter(word1), Counter(word2)
        return (
            True
            if sorted(word1Counter.values()) == sorted(word2Counter.values())
            and set(word1) == set(word2)
            else False
        )


s = Solution()
word1 = "cabbba"
word2 = "abbccc"
print(s.closeStrings(word1, word2))
