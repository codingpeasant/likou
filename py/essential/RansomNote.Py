# https://leetcode.com/problems/ransom-note/
# Hash Table,Counting
# Grind

from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for letter, count in ransom_note_count.items():
            if magazine_count[letter] < count:
                return False
        return True

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = Counter(magazine)

        for letter in ransomNote:
            if not magazineCount[letter]:
                return False
            magazineCount[letter] -= 1
        return True


s = Solution()
input = "aaac"
magazine = "acab"
print(s.canConstruct1(input, magazine))
