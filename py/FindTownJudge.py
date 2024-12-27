# https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        trustedCount = defaultdict(int)
        for a, b in trust:
            trustedCount[b] += 1
            trustedCount[a] -= 1

        for i in range(1, n + 1):
            if trustedCount[i] == n - 1:
                return i
        return -1


s = Solution()
n = 3
trust = [[1, 3], [2, 3]]
print(s.findJudge(n, trust))
