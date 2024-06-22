# https://leetcode.com/problems/restore-ip-addresses/description/
# Backtrack,String

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, n = [], len(s)

        def dfs(cur: str, start: int, parts: int):
            if parts == 4 and len(cur) == n + 4:
                res.append(cur[:-1])

            if parts > 4:
                return

            for i in range(start, start + 3):
                if i >= n:
                    break
                toAppend = int(s[start : i + 1])
                if (
                    toAppend > 255 or len(str(toAppend)) != i + 1 - start
                ):  # larger than 255 or leading 0
                    continue
                dfs(cur + str(toAppend) + ".", i + 1, parts + 1)

        dfs("", 0, 0)
        return res


s = Solution()
input = "101023"
print(s.restoreIpAddresses(input))
