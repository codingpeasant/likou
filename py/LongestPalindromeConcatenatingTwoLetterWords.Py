# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_counter = Counter(words)

        mid = False
        res = 0

        for word, count in words_counter.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    res += count
                else:
                    res += count - 1
                    mid = True
            else:
                res += 2 * min(count, words_counter[word[::-1]])
                words_counter[
                    word
                ] = 0  # make sure the reversed word doesn't consider it again

        if mid:  # make it double letter the mid of the palindrome
            res += 1

        return 2 * res


s = Solution()
input = ["lc", "cl", "gg"]
print(s.longestPalindrome(input))
