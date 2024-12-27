# https://leetcode.com/problems/decode-ways/

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s: str) -> int:
            if not s:
                return 1
            if s == "0":
                return 0
            if len(s) == 1:
                return dfs(s[1:])
            if len(s) > 1 and int(s[:2]) < 27:
                if int(s[:2]) < 10:
                    return 0
                return dfs(s[1:]) + dfs(s[2:])
            return dfs(s[1:])

        return dfs(s)


s = Solution()
str = "06"
print(s.numDecodings(str))
