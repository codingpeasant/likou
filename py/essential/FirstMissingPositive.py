# https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=rabvlt31
# Grind
# Neet

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(nums)

        # Place each positive integer num[i] at index i-1 if possible
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

    # TLE
    def firstMissingPositive1(self, nums: List[int]) -> int:
        minPositive, maxPositive = float("inf"), float("-inf")
        for num in nums:
            if num >= 0:
                minPositive = min(minPositive, num)
                maxPositive = max(maxPositive, num)
        if minPositive > 1:
            return 1

        numSet = set(num for num in nums if num >= 0)
        for num in range(minPositive, maxPositive + 1):
            if num not in numSet:
                return num
        return maxPositive + 1


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))  # 3
print(s.firstMissingPositive([3, 4, -1, 1]))  # 2
print(s.firstMissingPositive([7, 8, 9, 11, 12]))  # 1
print(s.firstMissingPositive1([1, 2, 0]))  # 3
print(s.firstMissingPositive1([3, 4, -1, 1]))  # 2
print(s.firstMissingPositive1([7, 8, 9, 11, 12]))  # 1
