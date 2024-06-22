# https://leetcode.com/problems/unique-morse-code-words/
# Hash Table

from typing import List, Set


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        map_morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        res = set()
        for word in words:
            morse = ""
            for letter in word:
                morse += map_morse[ord(letter) - ord("a")]
            res.add(morse)
        return len(res)


s = Solution()
input = ["gin", "zen", "gig", "msg"]
print(s.uniqueMorseRepresentations(input))
