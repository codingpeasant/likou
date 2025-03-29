# https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=oizxjoit
# Blind
# Grind
# Neet


class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedString = "".join([letter if letter.isalnum() else "" for letter in s]).lower()
        return processedString == processedString[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
