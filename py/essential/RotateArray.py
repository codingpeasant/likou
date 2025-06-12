# https://leetcode.com/problems/rotate-array/description/?envType=problem-list-v2&envId=rabvlt31
# Grind
# Neet

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
    
    def rotate1(self, nums: List[int], k: int) -> None:
        def reverse(input: List[int], start: int, end:int):
            while start < end:
                input[start],input[end] = input[end],input[start]
                start+=1
                end-=1
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        reverse(nums, 0 ,n-1)
        reverse(nums, 0 ,k-1)
        reverse(nums, k ,n-1)

s=Solution()
inputs = [1,2,3,4,5,6,7]
s.rotate1(inputs, 3)
print(inputs)