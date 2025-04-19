# https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(nums)

        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)

        # Find the first missing positive integer
        print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positive integers from 1 to n are present, return n + 1
        return n + 1

s=Solution()
print(s.firstMissingPositive([1,2,0])) # 3
print(s.firstMissingPositive([3,4,-1,1])) # 2
print(s.firstMissingPositive([7,8,9,11,12])) # 1