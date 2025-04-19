# https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Neet
# Grind


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        self.left, self.right = 0, 0

        def expand(i: int, j: int):
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                j += 1
                i -= 1
            if j - i > self.right - self.left:
                self.left = i
                self.right = j

        for i, _ in enumerate(s):
            expand(i, i)  # assume odd length, try to extend Palindrome as possible
            expand(i, i + 1)  # assume even length

        return s[self.left + 1 : self.right]


s = Solution()
print(s.longestPalindrome("cbbd"))
