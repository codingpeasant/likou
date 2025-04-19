# https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind
# Neet

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
    
    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram1("anagram", "nagaram"))
