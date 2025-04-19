# https://leetcode.com/problems/rotate-array/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]

s=Solution()
inputs = [1,2,3,4,5,6,7]
s.rotate(inputs, 3)
print(inputs)