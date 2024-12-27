# https://leetcode.com/problems/valid-parentheses/
# Stack
# Blind


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "}": "{", "]": "["}

        for letter in s:
            if letter in dict.values():  # {[(
                stack.append(letter)
            elif letter in dict.keys():
                if not stack or stack.pop() != dict[letter]:
                    return False
            else:
                return False
        return not stack


s = Solution()
input = "{(){}[]}"
print(s.isValid(input))
