# https://leetcode.com/problems/basic-calculator/
# https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
# Grind


class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == "+":
                stack.append(
                    v
                )  # only keep num in the stack as there will be a sum(stack)
            if op == "-":
                stack.append(-v)  # only keep num as there will be a sum(stack)
            if (
                op == "*"
            ):  # * and / has the higher priority so calculate number right away
                stack.append(
                    stack.pop() * v
                )  # for BC II and BC III: calculate immediately
            if op == "/":
                stack.append(
                    int(stack.pop() / v)
                )  # for BC II and BC III: calculate immediately

        i, num, stack, sign = (
            0,
            0,
            [],
            "+",
        )  # num is the current num read from the input, not calculated

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(
                    s[i]
                )  # the current number being read could be multiple digits so * 10
            elif s[i] in "+-*/":  # conclude the previous calculation
                update(sign, num)
                num, sign = 0, s[i]  # num is back to 0 after being put in the stack
            elif s[i] == "(":  # For BC I and BC III
                num, j = self.calculate(s[i + 1 :])
                i = i + j
            elif s[i] == ")":  # For BC I and BC III
                update(sign, num)
                return (
                    sum(stack),
                    i + 1,
                )  # if ), must conclude a recursive layer and return the result of this layer
            i += 1
        update(sign, num)
        return sum(stack)


s = Solution()
input = "(1+(4+5+2)-3)+(6+8)"
print(s.calculate(input))
input = "2*(5+5*2)/3+(6/2+8)"
print(s.calculate(input))
