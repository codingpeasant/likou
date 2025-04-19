# Blind
# Neet
# https://neetcode.io/problems/foreign-dictionary

from collections import defaultdict
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph, res = defaultdict(set), []
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] == word2[j]:
                    continue
                else:
                    graph[word1[j]].add(word2[j])
                    break

        visited = set()

        def dfs(char):
            if char in res:
                return  # skip already sorted letter (memory)
            if char in visited:
                return True  # cycle found

            visited.add(char)
            for nei in graph.get(char, []):
                if dfs(nei):
                    return True

            visited.remove(char)
            res.append(char)

        for char in graph.keys():
            if dfs(char):
                return ""

        return "".join(reversed(res))


s = Solution()
print(s.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
