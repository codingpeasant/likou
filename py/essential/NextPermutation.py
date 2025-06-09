# http://leetcode.com/problems/next-permutation/description/?envType=problem-list-v2&envId=rabvlt31
# Grind

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        i = n - 2
        # Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:  # If not the entire array in descending order
            # Find the first element that is greater than nums[i]
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the elements after the first decreasing element
        print(f"[i]: {i}, [j]: {j}")
        self.reverse(nums, i + 1, n - 1)
        # Reverse the elements in the range [start, end]
        # This is a two-pointer approach

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


s = Solution()
input = [3, 4, 2, 1]
s.nextPermutation(input)
print(input)
input = [1, 5, 1]
s.nextPermutation(input)
print(input)
input = [1, 3, 2, 4]
s.nextPermutation(input)
print(input)
