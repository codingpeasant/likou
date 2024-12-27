# https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=oizxjoit
# Blind
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        self.left, self.offset = 0, 0

        def expand(i: int, j: int):
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                j += 1
                i -= 1
            if j - i - 1 > self.offset:
                self.left = i + 1
                self.offset = j - i - 1

        for i, _ in enumerate(s):
            expand(i, i)  # assume odd length, try to extend Palindrome as possible
            expand(i, i + 1)  # assume even length

        return s[self.left : self.left + self.offset]


s = Solution()
print(s.longestPalindrome("cbbd"))
