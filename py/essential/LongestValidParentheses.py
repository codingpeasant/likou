# https://leetcode.com/problems/longest-valid-parentheses/
# Grind


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, left, res = (
            [],
            -1,
            0,
        )  #  when (), i = 1, left = -1 and max = 1 - (-1) = 2
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if not stack:
                    left = i
                else:
                    stack.pop()
                    if (
                        not stack
                    ):  # all pairs since left were matched, directly j - left
                        res = max(res, i - left)
                    else:
                        res = max(
                            res, i - stack[-1]
                        )  # some ( in the stack didn't match, go from the last ( in the stack
        return res


s = Solution()
print(s.longestValidParentheses(")()())"))
