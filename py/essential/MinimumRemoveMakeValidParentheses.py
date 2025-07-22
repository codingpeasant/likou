# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solutions/663204/super-simple-python-solution-with-explanation-faster-than-100-memory-usage-less-than-100/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        return "".join(s)


s = Solution()
print(s.minRemoveToMakeValid("a)b(c)d"))
