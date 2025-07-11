# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        used = [False] * 10  # 1~9
        self.res = []

        def backtrack(curNumber: list[int]):
            if len(curNumber) == n + 1:
                self.res = [str(cur) for cur in curNumber]
                return

            for i in range(1, 10):
                if used[i]:
                    continue
                curNumN = len(curNumber)
                if (
                    curNumN == 0
                    or (pattern[curNumN - 1] == "I" and i > curNumber[-1])
                    or (pattern[curNumN - 1] == "D" and i < curNumber[-1])
                ):
                    used[i] = True
                    curNumber.append(i)
                    backtrack(curNumber)
                    curNumber.pop()
                    used[i] = False

                if self.res:  # just stop and this is smallest
                    return

        backtrack([])
        return "".join(self.res)


s = Solution()
print(s.smallestNumber("IIIDIDDD"))
