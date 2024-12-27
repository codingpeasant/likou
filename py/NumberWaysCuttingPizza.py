# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/

from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @lru_cache(None)
        def has_apple(start_row, start_col, end_row, end_col):
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if pizza[r][c] == "A":
                        return True
            return False

        @lru_cache(None)
        def dp(start_row, start_col, num_slices_left):
            if num_slices_left == 1:
                if has_apple(start_row, start_col, len(pizza), len(pizza[0])):
                    return 1

            num_ways = 0
            for i in range(start_col + 1, len(pizza[0])):  # cut vertically
                if has_apple(start_row, start_col, len(pizza), i):
                    num_ways += dp(start_row, i, num_slices_left - 1)
            for j in range(start_row + 1, len(pizza)):  # cut horizontally
                if has_apple(start_row, start_col, j, len(pizza[0])):
                    num_ways += dp(j, start_col, num_slices_left - 1)
            return num_ways

        return dp(0, 0, k) % (10**9 + 7)


s = Solution()
pizza = ["A..", "AAA", "..."]
k = 3
print(s.ways(pizza, k))
