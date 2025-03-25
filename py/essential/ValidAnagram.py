# https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind

from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterTable = defaultdict(int)
        for letter in s:
            letterTable[letter] += 1
        for letter in t:
            if not letterTable.get(letter):
                return False
            letterTable[letter] -= 1
        return all(x == 0 for x in letterTable.values())


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
