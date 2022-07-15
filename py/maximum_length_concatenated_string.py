# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


from turtle import back
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        if len(arr) == 0:
            return max_len

        def backtrack(start, cur):  # start is to not repeat previous combinations
            nonlocal max_len

            if not is_unique(cur):
                return

            max_len = max(max_len, len(cur))

            for i in range(start, len(arr)):
                backtrack(start + 1, cur + arr[i])

        def is_unique(s: str) -> bool:
            return len(s) == len(set(s))

        backtrack(0, "")
        return max_len


s = Solution()

input = ["abcdefghijklmnopqrstuvwxyz"]

print(s.maxLength(input))
