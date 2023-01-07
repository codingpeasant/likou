# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        cur_max = 0
        for i in range(1, n - 1):  # skip index = 0
            cur_max = max(cur_max, height[i - 1])
            left_max[i] = cur_max

        cur_max = 0
        for i in range(n - 2, -1, -1):  # skip index = n-1
            cur_max = max(cur_max, height[i + 1])
            right_max[i] = cur_max

        res = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                res += water_level - height[i]
        return res


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height))
