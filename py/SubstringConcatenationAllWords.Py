# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        words_size = len(words)
        word_len = len(words[0])

        word_counts = {}
        for word in words:
            word_counts[word] = (
                1 if not word_counts.get(word) else word_counts[word] + 1
            )

        def concatStartsAt(concatStart: int) -> bool:
            copy = word_counts.copy()

            for iW in range(words_size):
                wordStart: int = concatStart + iW * word_len
                word: str = s[wordStart : wordStart + word_len]

                if not copy.get(word):
                    return False
                copy[word] -= 1

            return True

        return [
            iS for iS in range(s_len - words_size * word_len + 1) if concatStartsAt(iS)
        ]


s = Solution()
input = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(s.findSubstring(input, words))
