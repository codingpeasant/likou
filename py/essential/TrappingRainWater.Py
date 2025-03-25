# https://leetcode.com/problems/trapping-rain-water/
# Two Pointers
# Grind
# Neet
# https://leetcode.com/problems/trapping-rain-water/solutions/4486633/python3-stack-and-two-pointers-solutions/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # For bar[i], if we can find bar[j] and bar[k] where bar[j] > bar[i], bar[k] > bar[i] and j < i < k, then bar[i] is a valley bar: left_max and right_max is valley bar so 0<i<n-1
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # find the highest bar before the current index
        cur_max = 0
        for i in range(1, n - 1):  # skip index = 0 because there is no bar before 0
            cur_max = max(cur_max, height[i - 1])
            left_max[i] = cur_max

        # same, just after
        cur_max = 0
        for i in range(
            n - 2, -1, -1
        ):  # skip index = n-1 because there is no bar after n - 1
            cur_max = max(cur_max, height[i + 1])
            right_max[i] = cur_max

        res = 0
        for i in range(1, n - 1):  # again
            water_level = min(left_max[i], right_max[i]) - height[i]
            if water_level > 0:
                res += water_level
        return res


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height))
height = [4, 2, 0, 3, 2, 5]
print(s.trap(height))
