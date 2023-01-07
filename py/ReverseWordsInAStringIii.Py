# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())


s = Solution()
input = "Let's take LeetCode contest"
print(s.reverseWords(input))
