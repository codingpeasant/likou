# https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind

from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        @lru_cache(None)
        def dfs(stringLeft: str) -> bool:
            if stringLeft in wordDictSet or not stringLeft:
                return True
            for word in wordDictSet:
                if stringLeft.startswith(word) and dfs(stringLeft[len(word) :]):
                    return True
            return False

        return dfs(s)


s = Solution()
print(s.wordBreak("goalspecial", ["go", "goal", "goals", "special"]))
