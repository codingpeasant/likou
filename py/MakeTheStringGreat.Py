# https://leetcode.com/problems/make-the-string-great/


class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s
        stack = []

        for letter in s:
            if not stack or abs(ord(letter) - ord(stack[-1])) != 32:
                stack.append(letter)
            else:
                stack.pop()

        return "".join(stack)


s = Solution()
print(s.makeGood("leEeetcode"))
print(s.makeGood("abBAcC"))
