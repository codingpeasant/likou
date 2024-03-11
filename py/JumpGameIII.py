# https://leetcode.com/problems/jump-game-iii/description/

from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(index: int) -> bool:
            if 0 <= index < len(arr) and arr[index] >= 0:
                if arr[index] == 0:
                    return True
                arr[index] = -arr[
                    index
                ]  # flip the checked number to negative to indicate visited
                return dfs(index + arr[index]) or dfs(index - arr[index])
            return False

        return dfs(start)


s = Solution()
arr = [3, 0, 2, 1, 2]
start = 2
print(s.canReach(arr, start))
