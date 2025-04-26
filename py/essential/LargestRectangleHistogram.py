# https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # asc
        max_area = 0
        n = len(heights)

        for i in range(
            n + 1
        ):  # n+1 to make sure all the left heights in the stack can be calculated in the end
            current_height = (
                heights[i] if i < n else 0
            )  # 0 is for the same reason as n+1

            # if current_height is smaller than the previous seen heights, we cannot use the previous seen heights anymore in further calculation because including the previous seen max will not form a rectangle with the current_height included. So we have to calculate now by popping previous taller heights; if current_height is larger than the previous seen heights, we can still use the previous seen heights in further calculation because including the previous seen max will form a rectangle with the current_height included. So using a stack to keep the previous seen heights that can contribute to further calculations is a good idea. And this stack needs to be sorted or at least the top of the stack needs to be previous max to effectively compare with current_height.
            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1 # not stack when the heights are in decreasing order
                print([heights[i] if i < n else -1 for i in stack])
                print(
                    f"current_height: {current_height}, height: {height}, width: {width}"
                )
                max_area = max(max_area, height * width)
                print(f"area: {height * width}")

            stack.append(i)

        return max_area


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
