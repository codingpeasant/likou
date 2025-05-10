# https://leetcode.com/problems/word-break-ii/description/
# Neet

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        ans = []
        currentSolution = []
        def choose(i):
            if i == n:
                ans.append(" ".join(currentSolution))
                return
            for j in range(i, n):
                if s[i: j + 1] in wordDict:
                    currentSolution.append(s[i: j + 1])
                    choose(j + 1)
                    currentSolution.pop()
        choose(0)
        return ans
    
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        ans = []

        def dfs(stringLeft: str, curRes: List[str]):
            if not stringLeft:
                ans.append(" ".join(curRes.copy()))
                return
            for word in wordDictSet:
                if stringLeft.startswith(word):
                    curRes.append(word)
                    dfs(stringLeft[len(word):], curRes)
                    curRes.pop()
        dfs(s, [])
        return ans

# Example usage:
solution = Solution()

s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
print(solution.wordBreak1(s1, wordDict1))  # Output: ["cats and dog", "cat sand dog"]

s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
print(solution.wordBreak1(s2, wordDict2))  # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak1(s3, wordDict3))  # Output: []