# https://leetcode.com/problems/detect-capital/description/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(ord("a") - ord(letter) > 0 for letter in word):
            return True
        if all(ord(letter) - ord("a") >= 0 for letter in word):
            return True
        if word.istitle():
            return True
        return False


s = Solution()
word = "Falg"
print(s.detectCapitalUse(word))
