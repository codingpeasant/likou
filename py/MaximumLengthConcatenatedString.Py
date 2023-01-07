# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


from turtle import back
from typing import List


class Solution:
    max_len = 0

    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 0:
            return self.max_len

        def backtrack(start, cur):  # start is to not repeat previous combinations
            if not is_unique(cur):
                return

            self.max_len = max(self.max_len, len(cur))

            for i in range(start, len(arr)):
                backtrack(start + 1, cur + arr[i])

        def is_unique(s: str) -> bool:
            return len(s) == len(set(s))

        backtrack(0, "")
        return self.max_len


s = Solution()

input = ["a", "b", "c"]

print(s.maxLength(input))
