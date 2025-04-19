# https://leetcode.com/problems/daily-temperatures/
# Neet
# Grind

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        monoStack, res = [], [0] * n

        for i in range(n):
            while monoStack and temperatures[monoStack[-1]] < temperatures[i]:
                res[monoStack[-1]] = i - monoStack[-1]
                monoStack.pop()
            monoStack.append(i)

        return res


s = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temperatures))
