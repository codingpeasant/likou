# https://leetcode.com/problems/reverse-words-in-a-string/
# String


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


s = Solution()
input = "  a good   example   "
print(s.reverseWords(input))
