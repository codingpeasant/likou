# https://leetcode.com/problems/jump-game-v/description/

from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(i):
            path_len = 0
            for j in range(i + 1, i + d + 1):
                if len(arr) <= j or arr[j] >= arr[i]:
                    break
                path_len = max(dfs(j), path_len)
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                path_len = max(dfs(j), path_len)
            return path_len + 1

        longest_path = 0
        for i in range(len(arr)):
            longest_path = max(dfs(i), longest_path)
        return longest_path

s=Solution()
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
print(s.maxJumps(arr, d))