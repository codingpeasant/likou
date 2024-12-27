from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:  # lower one will not be considered
                left += 1
            else:  # if equal, needs to find 2 higher ones in between left and right and removing either makes no difference
                right -= 1
        return maxWater


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
