# https://leetcode.com/problems/palindrome-pairs/
# Grind

from typing import Dict, List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):  # empty string is also true
            return check == check[::-1]

        words: Dict = {word: i for i, word in enumerate(words)}  # convert to a map
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]  # also include empty string
                suf = word[j:]
                if is_palindrome(
                    pref
                ):  # aba|cb needs cb|aba|cb to be come a palindrome
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j != n and is_palindrome(
                    suf
                ):  # cb|aba needs cb|aba|bc to be come a palindrome
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


s = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(s.palindromePairs(words))
