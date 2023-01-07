# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        ans = 0
        curr_max = 0

        for a, d in properties:
            if d < curr_max:  # a is small and d is also smaller
                ans += 1
            else:
                curr_max = d
        return ans


s = Solution()
input = [[1, 5], [10, 4], [4, 3]]
print(s.numberOfWeakCharacters(input))
