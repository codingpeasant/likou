# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Sliding Window,Hash Table

from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        words_size = len(words)
        word_len = len(words[0])

        word_counts = Counter(words)

        def concatStartsAt(concatStart: int) -> bool:
            copy = word_counts.copy()

            for iW in range(words_size):
                wordStart: int = concatStart + iW * word_len  # move word_len at a time
                word: str = s[wordStart : wordStart + word_len]

                if not copy.get(word):
                    return False
                copy[word] -= 1

            return True

        return [
            iS
            for iS in range(s_len - words_size * word_len + 1)
            if concatStartsAt(iS)  # move one index at a time
        ]


s = Solution()
input = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(s.findSubstring(input, words))
