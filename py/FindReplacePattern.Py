# https://leetcode.com/problems/find-and-replace-pattern/


from collections import defaultdict
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        b = pattern

        def is_iso(a):
            return len(set(a)) == len(set(b)) == len(set(zip(a, b)))

        return filter(is_iso, words)

    def findAndReplacePattern1(self, words: List[str], pattern: str) -> List[str]:
        res = []

        def match(word) -> bool:
            dic_ab, dic_ba = defaultdict(str), defaultdict(str)
            for i in range(len(word)):
                if not word[i] in dic_ab:
                    dic_ab[word[i]] = pattern[i]
                if not pattern[i] in dic_ba:
                    dic_ba[pattern[i]] = word[i]
                if dic_ab[word[i]] != pattern[i] or dic_ba[pattern[i]] != word[i]:
                    return False
            return True

        for word in words:
            if match(word): res.append(word)
        return res


s = Solution()
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(list(s.findAndReplacePattern(words, pattern)))
print(s.findAndReplacePattern1(words, pattern))
