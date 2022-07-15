# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open, close, total):
            if len(cur) == total * 2:
                res.append(cur)
                return
            if open < total:
                backtrack(cur + "(", open + 1, close, total)
            if open > close:
                backtrack(cur + ")", open, close + 1, total)

        backtrack("", 0, 0, n)
        return res


s = Solution()
print(s.generateParenthesis(3))
