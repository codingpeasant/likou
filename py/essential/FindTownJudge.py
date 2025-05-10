# https://leetcode.com/problems/find-the-town-judge/
# Neet

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        return -1


s = Solution()
n = 3
trust = [[1, 3], [2, 3], [2, 1]]
print(s.findJudge(n, trust))
