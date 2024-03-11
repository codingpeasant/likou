# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount, res = 0, 0

        for char in s:
            if char == "1":
                oneCount += 1
            else:
                res = min(
                    oneCount, res + 1
                )  # option1: flip to 1 so it's prev+1; option2: don't flip it but flip all the previous 1s
        return res


s = Solution()
input = "010110"
print(s.minFlipsMonoIncr(input))
