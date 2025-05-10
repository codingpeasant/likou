# https://leetcode.com/problems/longest-turbulent-subarray/description/
# Neet

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        max_length = 1
        current_length = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                if i == 1 or arr[i - 1] <= arr[i - 2]: # equal means i-1 is the first element
                    current_length += 1
                else:
                    current_length = 2
            elif arr[i] < arr[i - 1]:
                if i == 1 or arr[i - 1] >= arr[i - 2]:
                    current_length += 1
                else:
                    current_length = 2
            else:
                current_length = 1
            max_length = max(max_length, current_length)
        return max_length

s=Solution()
arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(s.maxTurbulenceSize(arr))  # Output: 5
arr = [4, 8, 12, 16]
print(s.maxTurbulenceSize(arr))  # Output: 2