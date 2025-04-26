# https://neetcode.io/problems/valid-palindrome-ii
# Neet

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        for i in range(len(s)):
            newS = s[:i]+s[i+1:]
            if newS == newS[::-1]:
                return True
        return False
    
s = Solution()
input = "abca"
print(s.validPalindrome(input))
input = "abc"
print(s.validPalindrome(input))