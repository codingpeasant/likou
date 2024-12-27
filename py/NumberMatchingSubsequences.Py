# https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        res = 0

        for word in words:
            word_dict[word[0]].append(word)

        for ch in s:
            words_starting_ch = word_dict[ch]
            word_dict[ch] = []

            for word in words_starting_ch:
                if len(word) == 1:
                    res += 1  # Finished subsequence!
                else:
                    word_dict[word[1]].append(
                        word[1:]
                    )  # remove the first char and start from the rest

        return res


s = Solution()
input_str = "abcde"
words = ["a", "bb", "acd", "ace"]

print(s.numMatchingSubseq(input_str, words))
