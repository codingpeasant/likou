# https://leetcode.com/problems/generate-parentheses/
# Neet

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open, close):
            if len(cur) == n * 2:
                res.append(cur)
                return
            if open < n:
                backtrack(cur + "(", open + 1, close)
            if open > close:
                backtrack(cur + ")", open, close + 1)

        backtrack("", 0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))
