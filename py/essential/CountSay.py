# https://leetcode.com/problems/count-and-say/description/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prevStr = self.countAndSay(n - 1)
        n, i = len(prevStr), 0
        res = []
        while i < n:
            curL = prevStr[i]
            curCount = 1
            i += 1
            while i < n and prevStr[i] == curL:
                curCount += 1
                i += 1
            res.append(str(curCount) + curL)
        return "".join(res)


s = Solution()
print(s.countAndSay(10))
