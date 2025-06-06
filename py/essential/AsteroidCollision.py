# https://leetcode.com/problems/asteroid-collision/description/?envType=problem-list-v2&envId=rabvlt31
# Grind
# Neet

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if (
                    stack[-1] < -asteroid
                ):  # only stack[-1] explodes and moves on to the next one in the stack
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:  # both explode
                    stack.pop()
                break  # the negative asteroid explodes
            else:  # while ... else
                stack.append(asteroid)
        return stack


s = Solution()
print(s.asteroidCollision([5, 10, -5]))  # [5, 10]
print(s.asteroidCollision([8, -8]))  # []
print(s.asteroidCollision([10, 2, -5]))  # [10]
