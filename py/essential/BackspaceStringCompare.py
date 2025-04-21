# https://leetcode.com/problems/backspace-string-compare/description/?envType=problem-list-v2&envId=rabvlt31
# Grind


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if char == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in t:
            if char == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        return stack1 == stack2


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a#c", "b"))
print(s.backspaceCompare("a##c", "#a#c"))
