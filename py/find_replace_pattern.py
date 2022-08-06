# https://leetcode.com/problems/find-and-replace-pattern/


from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        b = pattern

        def is_iso(a):
            return len(set(a)) == len(set(b)) == len(set(zip(a, b)))

        return filter(is_iso, words)


s = Solution()
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(list(s.findAndReplacePattern(words, pattern)))
