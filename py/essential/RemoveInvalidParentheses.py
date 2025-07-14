# https://leetcode.com/problems/remove-invalid-parentheses/description/

from typing import List


class Solution:
    def removeInvalidParentheses1(self, s: str) -> List[str]:
        # leftCount: how many "(" is larger than ")"
        def isValid(input: str) -> tuple[bool, int, int]:
            stack, leftCount, rightCount = [], 0, 0
            for i in range(len(input)):
                if input[i] == "(":
                    stack.append(input[i])
                    leftCount += 1
                if input[i] == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                        leftCount -= 1
                    else:
                        rightCount += 1
            return leftCount == rightCount == 0, leftCount, rightCount

        def dfs(input: str, leftCount: int, rightCount: int):
            visited.add(input)
            if isValid(input)[0]:
                res.append(input)
            for i, letter in enumerate(input):
                if letter != "(" and letter != ")":
                    continue
                if (letter == "(" and leftCount <= 0) or (
                    letter == ")" and rightCount <= 0
                ):
                    continue
                if not input[:i] + input[i + 1 :] in visited:
                    dfs(
                        input[:i] + input[i + 1 :],
                        leftCount - (letter == "("),
                        rightCount - (letter == ")"),
                    )

        res = []
        visited = set()
        valid, leftCount, rightCount = isValid(s)

        if valid:
            return [s]
        dfs(s, leftCount, rightCount)
        return res


s = Solution()

print("-----------")
print(s.removeInvalidParentheses1("(a)())()"))
print(s.removeInvalidParentheses1(")))((("))
print(s.removeInvalidParentheses1("(((s)))"))
