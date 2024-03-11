# https://leetcode.com/problems/verifying-an-alien-dictionary/

from collections import defaultdict
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letterOrder, n = defaultdict(int), len(words)
        for i, letter in enumerate(order):
            letterOrder[letter] = i

        for i in range(1, n):
            word1 = words[i - 1]
            word2 = words[i]
            word1Len = len(word1)
            word2Len = len(word2)
            length = word1Len if word1Len <= word2Len else word2Len
            increasing = False
            for j in range(length):
                if letterOrder[word1[j]] > letterOrder[word2[j]]:
                    return False
                if letterOrder[word1[j]] < letterOrder[word2[j]]:
                    increasing = True
                    break
            if not increasing and word1Len > word2Len:
                return False
        return True


s = Solution()
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))
