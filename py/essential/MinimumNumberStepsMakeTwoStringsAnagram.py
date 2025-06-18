# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        more, less = 0, 0
        for key, value in sCounter.items():
            if value > tCounter[key]:
                more += value - tCounter[key]
            elif value < tCounter[key]:
                less += tCounter[key] - value
        return max(more, less)


s = Solution()
print(s.minSteps("bab", "aba"))
print(s.minSteps("leetcode", "practice"))
print(s.minSteps("anagram", "mangaar"))
