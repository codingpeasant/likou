# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        cache = defaultdict(
            str
        )  # cannot just use @lru_cache on dfs(ch) because the same input ch might return different res
        for a, b in zip(s1, s2):
            if a != b:
                graph[a].add(b)
                graph[b].add(a)

        visited = set()

        def dfs(ch) -> str:
            visited.add(ch)
            res = ch

            for nei in graph[ch]:
                if nei not in visited:
                    res = min(res, dfs(nei))
            return res

        ret = []
        for letter in baseStr:
            visited.clear()
            if letter in cache.keys():
                ret.append(cache[letter])
            else:
                minLetter = dfs(letter)
                cache[letter] = minLetter
                ret.append(minLetter)
        return "".join(ret)


s = Solution()
s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(s.smallestEquivalentString(s1, s2, baseStr))
