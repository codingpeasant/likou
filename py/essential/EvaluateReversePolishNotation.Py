# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Grind
# Neet

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))
        return stack[0]


s = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(tokens))
