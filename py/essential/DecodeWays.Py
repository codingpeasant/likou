# https://leetcode.com/problems/decode-ways/
# Blind

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s: str) -> int:
            if not s:
                return 1
            if len(s) == 1:
                return 0 if s == "0" else 1
            if int(s[:2]) < 27:
                if int(s[:2]) < 10:
                    return 0
                return dfs(s[1:]) + dfs(s[2:])
            return dfs(s[1:])

        return dfs(s)


s = Solution()
strInput = "06"
print(s.numDecodings(strInput))
