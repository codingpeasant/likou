# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))


s = Solution()
input = "  a good   example   "
print(s.reverseWords(input))
