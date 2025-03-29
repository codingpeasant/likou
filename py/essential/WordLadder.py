# https://leetcode.com/problems/word-ladder/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from collections import deque
from itertools import product
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isAdjacent(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            return count == 1

        n = len(beginWord)
        res = 0
        visited = set() # to avoid a circle
        q = deque([beginWord])
        while q:
            qSize = len(q)
            for _ in range(qSize):
                curWord = q.popleft()
                if curWord == endWord:
                    return res + 1
                for word in wordList:
                    if word not in visited and isAdjacent(curWord, word):
                        visited.add(word)
                        q.append(word)
            res += 1
        return 0


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(s.ladderLength(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(s.ladderLength(beginWord, endWord, wordList))
