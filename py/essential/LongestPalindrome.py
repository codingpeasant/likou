# https://leetcode.com/problems/longest-palindrome/?envType=problem-list-v2&envId=rab78cw1
# Grind


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterSet, count = set(), 0
        for letter in s:
            if letter in letterSet:
                letterSet.remove(
                    letter
                )  # if there was a matching before, add 1 palindrome
                count += 1
            else:
                letterSet.add(letter)
        if letterSet:
            return (
                count * 2 + 1
            )  # pick one left in the set as the center of the palindrome string
        return count * 2


s = Solution()
print(s.longestPalindrome("abccccdd"))
