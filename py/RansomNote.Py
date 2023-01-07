# https://leetcode.com/problems/ransom-note/

from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for letter, count in ransom_note_count.items():
            if magazine_count[letter] < count:
                return False
        return True


s = Solution()
input = "aaq"
magazine = "acab"
print(s.canConstruct(input, magazine))
