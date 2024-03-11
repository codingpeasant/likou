# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols, islands, seen = defaultdict(list), defaultdict(list), 0, set()

        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)

        def dfs(i, j):
            for jj in rows[i]:  # other stones on the same row
                if (i, jj) not in seen:
                    seen.add((i, jj))
                    dfs(i, jj)
            for ii in cols[j]:
                if (ii, j) not in seen:
                    seen.add((ii, j))
                    dfs(ii, j)

        for i, j in stones:
            if (i, j) not in seen:
                islands += 1
                seen.add((i, j))
                dfs(i, j)

        return len(stones) - islands


s = Solution()
stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(s.removeStones(stones))
