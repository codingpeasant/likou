# https://leetcode.com/problems/sort-characters-by-frequency/
# Sorting,Hash Table

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        strCounter = Counter(s)
        strCounter = sorted(strCounter.items(), key=lambda item: item[1], reverse=True)
        res = []
        for letter, freq in strCounter:
            res += [letter for _ in range(freq)]

        return "".join(res)


s = Solution()
input = "tree"
print(s.frequencySort(input))
