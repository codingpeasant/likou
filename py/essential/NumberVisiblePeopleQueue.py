# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/


from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []  # desc
        n = len(heights)
        res = [0] * n
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                lastIndex = stack.pop()
                res[
                    lastIndex
                ] += 1  # not index - lastIndex because 10 cannot see 5 because of 8
            if stack:
                res[stack[-1]] += 1
            stack.append(index)

        return res


s = Solution()
print(s.canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(s.canSeePersonsCount([10, 6, 5, 4, 11, 9]))
