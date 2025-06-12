# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        reversedS = s[::-1]
        for i in range(len(s)):
            cur = reversedS[i:]
            if s.startswith(cur):
                return reversedS[:i] + s
        return reversedS+s
    
    def shortestPalindromeRollingHash(self, s: str) -> str:
        base = 131
        mod = 10**9 + 7
        n = len(s)
        prefix = suffix = 0
        mul = 1
        idx = 0
        for i, c in enumerate(s):
            prefix = (prefix * base + (ord(c) - ord('a') + 1)) % mod
            suffix = (suffix + (ord(c) - ord('a') + 1) * mul) % mod
            mul = (mul * base) % mod
            if prefix == suffix:
                idx = i + 1
        return s if idx == n else s[idx:][::-1] + s

s=Solution()
print(s.shortestPalindrome("abcd"))
print(s.shortestPalindromeRollingHash("abcd"))