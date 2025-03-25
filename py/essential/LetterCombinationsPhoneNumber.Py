# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Grind
# Neet

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(cur, index):
            if index >= len(digits):
                res.append(cur)
                return
            letters = dic[digits[index]]
            for letter in letters:
                backtrack(cur + letter, index + 1)

        backtrack("", 0)
        return res


s = Solution()
digits = "23"
print(s.letterCombinations(digits))
