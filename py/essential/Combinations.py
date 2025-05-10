# https://leetcode.com/problems/combinations/description/
# Neet

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(cur: List[int], start:int):
            if len(cur) == k:
                res.append(cur.copy())
                return
            for i in range(start, n+1):
                cur.append(i)
                backtrack(cur, i+1)
                cur.pop()

        backtrack([], 1)
        return res

s=Solution()
print(s.combine(4,2))