# https://leetcode.com/problems/palindrome-partitioning/description/
# Neet

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, n = [], len(s)

        def isPalindrome(input: str) -> bool:
            return input == input[::-1]

        def dfs(cur: List[str], start: int):
            if start >= n:
                res.append(cur.copy())

            for i in range(start, n):
                subStr = s[start : i + 1]
                if isPalindrome(subStr):
                    cur.append(subStr)
                    dfs(cur, i + 1)
                    cur.pop()

        dfs([], 0)
        return res


s = Solution()
input = "aabbaab"
print(s.partition(input))
